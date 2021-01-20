from typing import Callable, TypeVar
from expression.collections import Seq, seq

A = TypeVar("A")
B = TypeVar("B")


def map(mapper: Callable[[A], B], xs: Seq[A]) -> Seq[B]:
    return xs.map(mapper)


delay = seq.delay
rangeNumber = seq.range
singleton = seq.singleton


__all__ = ["delay", "map", "rangeNumber", "singleton"]
