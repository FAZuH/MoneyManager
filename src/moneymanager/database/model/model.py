from dataclasses import Field
from typing import Any, ClassVar, Protocol


class Model[T](Protocol):
    __dataclass_fields__: ClassVar[
        dict[str, Field[Any]]
    ]  # From _typeshed.DataclassInstance protocol

    @property
    def primary_key(self) -> T: ...
    @classmethod
    def primary_field(cls) -> str: ...
