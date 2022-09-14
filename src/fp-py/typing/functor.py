from abc import abstractmethod
from typing import TypeVar, Protocol, Callable, runtime_checkable

TSource = TypeVar("TSource", covariant=True)
TResult = TypeVar("TResult")


@runtime_checkable
class Functor(Protocol[TSource]):
    @abstractmethod
    def map(self, fn: Callable[[TSource], TResult]) -> "Functor[TResult]":
        raise NotImplemented
