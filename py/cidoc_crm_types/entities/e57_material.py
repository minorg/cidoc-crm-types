from .e55_type import E55Type
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E57Material(E55Type):
    P126_was_employed_in: Tuple[object, ...] = ()  # Range: E11Modification
    P45_is_incorporated_in: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P68_use_foreseen_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
