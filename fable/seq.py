from expression.collections import seq


def map(mapper, seq):
    return seq.map(mapper)


rangeNumber = seq.range
delay = frozenlist.singleton

__all__ = ["ofArray", "singleton"]
