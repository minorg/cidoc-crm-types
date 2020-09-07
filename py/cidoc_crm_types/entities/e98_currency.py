
from dataclasses import dataclass
from .e55_type import E55Type
from .e58_measurement_unit import E58MeasurementUnit

@dataclass
class E98Currency(E55Type, E58MeasurementUnit):
    pass
