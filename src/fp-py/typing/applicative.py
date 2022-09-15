from __future__ import annotations

from abc import abstractmethod
from typing import Callable, Protocol, TypeVar, runtime_checkable

TSource = TypeVar("TSource")
TResult = TypeVar("TResult")


@runtime_checkable
class Applicative(Protocol[TSource, TResult]):
    @abstractmethod
    def apply(self, something):
        raise NotImplemented

    @classmethod
    @abstractmethod
    def pure(cls, fn: Callable[[TSource], TResult]) -> Applicative[TSource, TResult]:
        raise NotImplemented
