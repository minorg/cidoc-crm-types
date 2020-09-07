
from dataclasses import dataclass
from .e58_measurement_unit import E58MeasurementUnit
from .e55_type import E55Type

@dataclass
class E98Currency(E58MeasurementUnit, E55Type):
    pass
