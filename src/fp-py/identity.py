from functools import partial
from typing import TypeVar, Generic, Callable
from __future__ import annotations

from .typing import Functor, Monad, Applicative

TSource = TypeVar("TSource")
TResult = TypeVar("TResult")


class Identity(Generic[TSource]):
    def __init__(self, value: TSource) -> None:
        self._value = value

    # utils
    # =====

    def run(self) -> TSource:
        return self._value

    # Functor
    # =======

    def map(self, mapper: Callable[[TSource], TResult]) -> Identity[TResult]:
        return Identity(mapper(self._value))

    # Applicative
    # ===========

    @classmethod
    def pure(cls, value: TSource):
        """Applicative functor constructor

        This value should be function
        """
        return Identity(value)

    def apply(
        self: Identity[Callable[[TSource], TResult]], something: Identity[TSource]
    ) -> Identity[TResult | partial[TResult]]:
        def mapper(other_value):
            try:
                return self._value(other_value)
            except TypeError:
                return partial(self._value, other_value)

        return something.map(mapper)

    # Monad
    # =====

    @classmethod
    def unit(cls, value: TSource) -> "Identity[TSource]":
        return Identity(value)

    def bind(self, func: Callable[[TSource], Identity[TResult]]) -> Identity[TResult]:
        return func(self._value)

    # magic method
    # =====

    def __call__(self) -> TSource:
        return self.run()

    def __eq__(self, other) -> bool:
        return self._value == other()

    def __str__(self) -> str:
        return f"Identity({self._value})"

    def __repr__(self) -> str:
        return str(self)


assert isinstance(Identity, Functor)
assert isinstance(Identity, Applicative)
assert isinstance(Identity, Monad)
