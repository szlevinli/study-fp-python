from __future__ import annotations

from abc import abstractmethod
from typing import Protocol, TypeVar, runtime_checkable

TSource = TypeVar("TSource")


@runtime_checkable
class Monoid(Protocol[TSource]):
    @classmethod
    @abstractmethod
    def empty(cls) -> Monoid[TSource]:
        raise NotImplemented

    def __add__(self, other):
        raise NotImplemented
