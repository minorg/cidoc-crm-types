from .e90_symbolic_object import E90SymbolicObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E41Appellation(E90SymbolicObject):
    P139_has_alternative_form: Tuple[object, ...] = ()  # Range: E41Appellation
    P1_identifies: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P76_provides_access_to: Tuple[object, ...] = ()  # Range: E39Actor
