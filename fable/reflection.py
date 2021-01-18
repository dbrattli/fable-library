from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, List, Optional, Type, Union

from .types import Union as FsUnion

Constructor = Callable[..., Any]

EnumCase = Union[str, int]
FieldInfo = Union[str, "TypeInfo"]


@dataclass
class CaseInfo:
    declaringType: TypeInfo
    tag: int
    name: str
    fields: List[FieldInfo]


@dataclass
class TypeInfo:
    fullname: str
    generics: Optional[List[TypeInfo]] = None
    construct: Optional[Constructor] = None
    parent: Optional[TypeInfo] = None
    fields: Optional[Callable[[], List[FieldInfo]]] = None
    cases: Optional[Callable[[], List[CaseInfo]]] = None
    enum_cases: Optional[List[EnumCase]] = None

    def __str__(self) -> str:
        return full_name(self)


def class_type(
    fullname: str,
    generics: Optional[List[TypeInfo]] = None,
    construct: Optional[Constructor] = None,
    parent: Optional[TypeInfo] = None,
) -> TypeInfo:
    return TypeInfo(fullname, generics, construct, parent)


def union_type(
    fullname: str,
    generics: List[TypeInfo],
    construct: Type[FsUnion],
    cases: Callable[[], List[List[FieldInfo]]],
) -> TypeInfo:
    def fn() -> List[CaseInfo]:
        nonlocal construct

        caseNames: List[str] = construct.cases()
        mapper: Callable[[int, List[FieldInfo]], CaseInfo] = lambda i, fields: CaseInfo(t, i, caseNames[i], fields)
        return [mapper(i, x) for i, x in enumerate(cases())]

    t: TypeInfo = TypeInfo(fullname, generics, construct, None, None, fn, None)
    return t


def record_type(
    fullname: str, generics: List[TypeInfo], construct: Constructor, fields: Callable[[], List[FieldInfo]]
) -> TypeInfo:
    return TypeInfo(fullname, generics, construct, fields=fields)


def full_name(t: TypeInfo) -> str:
    gen = t.generics if t.generics is not None else []
    if len(gen):
        return t.fullname + "[" + ",".join(map(full_name, gen)) + "]"

    return t.fullname


obj_type: TypeInfo = TypeInfo(fullname="System.Object")
unit_type: TypeInfo = TypeInfo("Microsoft.FSharp.Core.Unit")
char_type: TypeInfo = TypeInfo("System.Char")
string_type: TypeInfo = TypeInfo("System.String")
bool_type: TypeInfo = TypeInfo("System.Boolean")
int8_type: TypeInfo = TypeInfo("System.SByte")
uint8_type: TypeInfo = TypeInfo("System.Byte")
int16_type: TypeInfo = TypeInfo("System.Int16")
uint16_type: TypeInfo = TypeInfo("System.UInt16")
int32_type: TypeInfo = TypeInfo("System.Int32")
uint32_type: TypeInfo = TypeInfo("System.UInt32")
float32_type: TypeInfo = TypeInfo("System.Single")
float64_type: TypeInfo = TypeInfo("System.Double")
decimal_type: TypeInfo = TypeInfo("System.Decimal")
