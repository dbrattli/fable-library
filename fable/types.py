from __future__ import annotations

from abc import abstractstaticmethod
from typing import Any, List

from .util import IComparable


class Union(IComparable["Union"]):
    def __init__(self):
        self.tag: int
        self.fields: List[int] = []

    @abstractstaticmethod
    def cases() -> List[str]:
        ...

    @property
    def name(self) -> str:
        return self.cases()[self.tag]

    def to_JSON(self) -> str:
        raise NotImplementedError
        # return str([self.name] + self.fields) if len(self.fields) else self.name

    def __str__(self) -> str:
        if not len(self.fields):
            return self.name

        fields = ""
        with_parens = True
        if len(self.fields) == 1:
            field = str(self.fields[0])
            with_parens = field.find(" ") >= 0
            fields = field
        else:
            fields = ", ".join(map(str, self.fields))

        return self.name + (" (" if with_parens else " ") + fields + (")" if with_parens else "")

    def __hash__(self) -> int:
        hashes = map(hash, self.fields)
        return hash([hash(self.tag), *hashes])

    def __eq__(self, other: Any) -> bool:
        if self is other:
            return True
        if not isinstance(other, Union):
            return False

        if self.tag == other.tag:
            return self.fields == other.fields

        return False

    def __lt__(self, other: Any) -> bool:
        if self.tag == other.tag:
            return self.fields < other.fields

        return self.tag < other.tag


class Record(IComparable["Record"]):
    def toJSON(self) -> str:
        return recordToJSON(this)

    def toString(self) -> str:
        return recordToString(self)

    def GetHashCode(self) -> int:
        return recordGetHashCode(self)

    def Equals(self, other: Record) -> bool:
        return recordEquals(self, other)

    def CompareTo(self, other: Record) -> int:
        return recordCompareTo(self, other)


class Attribute:
    pass


__all__ = ["Attribute", "Union"]
