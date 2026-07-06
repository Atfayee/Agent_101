from typing import TypeVar, ParamSpec, Callable
from app.tools.errors import ToolTemporaryError
from functools import wraps
import random, time

R = TypeVar("R")
P = ParamSpec("P")


def retry_with_backoff(
    max_attempts: int = 3,
    base_delay: float = 0.5,
    max_delay: float = 4.0,
    jitter: bool = True
):
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_error: Exception | None = None

            for attempt in range(1, max_attempts + 1):

                try:
                    return func(*args, **kwargs)
                
                except ToolTemporaryError as error:

                    last_error = error

                    if attempt == max_attempts:
                        raise ToolTemporaryError(f"retry reach {max_attempts} attempts")
                    
                    delay = min(base_delay * (2 ** (attempt - 1)), max_delay)

                    if jitter:
                        delay = delay + random.uniform(0, delay * 0.25)

                    time.sleep(delay)
                raise last_error
            return wrapper
        return decorator
