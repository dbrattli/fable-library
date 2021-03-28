from typing import Callable, TypeVar
from expression.collections import Seq, seq, frozenlist

A = TypeVar("A")
B = TypeVar("B")


def map(mapper: Callable[[A], B], xs: Seq[A]) -> Seq[B]:
    return Seq(xs).map(mapper)


def filter(predicate: Callable[[A], bool], xs: Seq[A]) -> Seq[A]:
    return Seq(xs).filter(predicate)


def skip(count: int, xs: Seq[A]) -> Seq[A]:
    return Seq(xs).skip(count)


def length(xs):
    return Seq(xs).length()


def empty():
    return seq.empty


delay = seq.delay
head = seq.head
rangeNumber = seq.range
singleton = seq.singleton
append = seq.concat
ofList = seq.of_list
toList = frozenlist.of_seq
concat = seq.concat

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
