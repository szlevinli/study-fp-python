from __future__ import annotations

from abc import abstractmethod
from typing import Callable, Protocol, TypeVar, runtime_checkable

TSource = TypeVar("TSource")
TResult = TypeVar("TResult")


@runtime_checkable
class Monad(Protocol[TSource]):
    @abstractmethod
    def bind(self, fn: Callable[[TSource], Monad[TResult]]) -> Monad[TResult]:
        """Monad bind method.

        Haskell: (>>=) :: m a -> (a -> m b) -> m b

        Python: bind(self: Monad[A], func: Callable[[A], B]) -> Monad[B]

        This is the mother of all methods. It's hard to describe what it
        does, because it can be used for pretty much anything:

        * Transformation, for projecting Monadic values and functions.
        * Composition, for composing Monadic functions.
        * Chaining, for chaining of function as a monadic value.
        * Combining, for combining monadic values.
        * Sequencing, of Monadic function.
        * Flatting, of nested Monadic values.
        * Variable substitution, assign values to variables.

        The Monad doesn't specify what is happening, only that whatever
        is happening satisfies the laws of associativity and identity.

        Return a new Monad.
        """
        raise NotImplemented

    @classmethod
    @abstractmethod
    def unit(cls, value: TSource) -> Monad[TSource]:
        """Wrap a value in a default context.

        Haskell: return :: a -> m a

        Inject a value into the monadic type. Since return is a reserved
        word in Python, we align with Scala and use the name unit
        instead.
        """
        raise NotImplemented
