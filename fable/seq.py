from typing import Callable, TypeVar
from expression.collections import Seq, seq

A = TypeVar("A")
B = TypeVar("B")


def map(mapper: Callable[[A], B], xs: Seq[A]) -> Seq[B]:
    return xs.map(mapper)


delay = seq.delay
rangeNumber = seq.range
singleton = seq.singleton
empty = seq.empty
append = seq.concat

__all__ = ["delay", "empty", "map", "rangeNumber", "singleton"]
