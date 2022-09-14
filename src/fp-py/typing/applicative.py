from abc import abstractmethod
from typing import TypeVar, Protocol, Callable, runtime_checkable

TSource = TypeVar("TSource", covariant=True)
TResult = TypeVar("TResult", covariant=True)


@runtime_checkable
class Applicative(Protocol[TSource, TResult]):
    @abstractmethod
    def apply(self, something):
        raise NotImplemented
