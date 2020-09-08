from .e55_type import E55Type
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E56Language(E55Type):
    P72_is_language_of: Tuple[object, ...] = ()  # Range: E33LinguisticObject
