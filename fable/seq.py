from typing import Callable, TypeVar
from expression.collections import Seq, seq

A = TypeVar("A")
B = TypeVar("B")


def map(mapper: Callable[[A], B], xs: Seq[A]) -> Seq[B]:
    return xs.map(mapper)


def skip(count: int, xs: Seq[A]) -> Seq[A]:
    return xs.skip(count)


def length(xs):
    return len(xs)


delay = seq.delay
head = seq.head
rangeNumber = seq.range
singleton = seq.singleton
empty = seq.empty
append = seq.concat

__all__ = [
    "delay",
    "empty",
    "head",
    "map",
    "length",
    "rangeNumber",
    "singleton",
    "skip",
]
