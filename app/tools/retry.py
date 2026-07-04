from typing import Callable, ParamSpec, TypeVar
from tools.error_handling import ToolTemporaryError
from functools import wraps
import time, random

P = ParamSpec("P")
R = TypeVar("R")

def retry_with_backoff(
    max_attempts: int = 3,
    base_delay: float = 0.5,
    max_delay: float = 2.0,
    jitter: bool = True
):
    """
    Only retries tool temporary error.
    Does not retry:
    - ToolInputError
    - ToolFataError
    - unknown errors

    Args:
        max_attempts: maximum number of retry
        base_delay: first retry delay in seconds
        max_delay: maximum retry delay cap
        jitter: wthether to add random delay
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:

            last_error: Exception | None = None

            for attempt in range(1, max_attempts + 1):

                try:
                    return func(*args, **kwargs)
                
                except ToolTemporaryError as error:

                    last_error = error

                    if attempt == max_attempts:

                        raise ToolTemporaryError(
                            f"tool failure after {max_attempts} attemps"
                            f"error: {last_error}"
                        )
                    
                    delay = min(base_delay * (2 ** (attempt - 1)), max_delay)

                    if jitter:

                        delay += random.uniform(0, delay * 0.25)

                    time.sleep(delay)

            raise last_error
        
        return wrapper
    
    return decorator