from __future__ import annotations

from abc import abstractmethod
from typing import Callable, Protocol, TypeVar, runtime_checkable

TSource = TypeVar("TSource", covariant=True)
TResult = TypeVar("TResult")


@runtime_checkable
class Functor(Protocol[TSource]):
    @abstractmethod
    def map(self, fn: Callable[[TSource], TResult]) -> Functor[TResult]:
        raise NotImplemented
