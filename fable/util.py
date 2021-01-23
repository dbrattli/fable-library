from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any, Optional

T = TypeVar("T")


class IEquatable(Generic[T], ABC):
    def GetHashCode(self) -> int:
        return self.GetHashCode()

    def Equals(self, other: T) -> bool:
        return self.Equals(other)

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        return NotImplemented

    @abstractmethod
    def __hash__(self) -> int:
        raise NotImplementedError


class IComparable(IEquatable[T]):
    def CompareTo(self, other: T) -> int:
        if self < other:
            return -1
        elif self == other:
            return 0
        return 1

    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        raise NotImplementedError


def equals(a, b):
    return a == b


def assertEqual(actual: T, expected: T, msg: Optional[str] = None) -> None:
    if actual != expected:
        raise Exception(msg or f"Expected: ${expected} - Actual: ${actual}")


def assertNotEqual(actual: T, expected: T, msg: Optional[str] = None) -> None:
    if actual == expected:
        raise Exception(msg or f"Expected: ${expected} - Actual: ${actual}")