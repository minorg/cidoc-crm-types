from .e63_beginning_of_existence import E63BeginningofExistence
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E67Birth(E63BeginningofExistence):
    P97_from_father: Tuple[object, ...] = ()  # Range: E21Person
