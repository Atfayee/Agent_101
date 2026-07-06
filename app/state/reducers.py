from typing import TypeVar

T = TypeVar("T")

def append_list(old: list[T] | None, new: list[T] | None) -> list[T]:
    return (old or []) + (new or [])

def merge_int(old: T | None, new: T | None) -> T:
    return (old or 0) + (new or 0)