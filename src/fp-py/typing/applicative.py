from abc import abstractmethod
from typing import Protocol, TypeVar, runtime_checkable

TSource = TypeVar("TSource", covariant=True)
TResult = TypeVar("TResult", covariant=True)


@runtime_checkable
class Applicative(Protocol[TSource, TResult]):
    @abstractmethod
    def apply(self, something):
        raise NotImplemented
