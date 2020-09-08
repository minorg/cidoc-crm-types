from .e55_type import E55Type
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E58MeasurementUnit(E55Type):
    P91_is_unit_of: Tuple[object, ...] = ()  # Range: E54Dimension
