# flake8: noqa

from typing import Any, Callable, TypeVar

from expression.collections import FrozenList

A = TypeVar("A")
B = TypeVar("B")


def empty() -> FrozenList[Any]:
    return FrozenList.empty()


def map(mapper: Callable[[A], B], lst: FrozenList[A]) -> FrozenList[B]:
    return lst.map(mapper)


def filter(predicate: Callable[[A], bool], lst: FrozenList[A]) -> FrozenList[A]:
    return lst.filter(predicate)


def length(xs):
    return len(xs)


ofArray = FrozenList.of_seq
ofSeq = FrozenList.of_seq
singleton = FrozenList.singleton

__all__ = ["length", "map", "ofArray", "ofSeq", "singleton"]
