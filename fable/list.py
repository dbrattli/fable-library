# flake8: noqa

from expression.collections import frozenlist


def empty():
    return frozenlist.empty

def map(mapper, lst):
    return lst.map(mapper)

def filter(predicate, lst):
    return lst.filter(predicate)

ofArray = frozenlist.of_seq
ofSeq = frozenlist.of_seq
singleton = frozenlist.singleton

__all__ = ["map", "ofArray", "ofSeq", "singleton"]
