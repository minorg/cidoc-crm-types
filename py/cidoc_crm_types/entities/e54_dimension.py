from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E54Dimension(E1CRMEntity):
    P191i_was_duration_of: Tuple[object, ...] = ()  # Range: E52TimeSpan
    P40_was_observed_in: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P43_is_dimension_of: Tuple[object, ...] = ()  # Range: E70Thing
    P90_has_value: Tuple[object, ...] = ()  # Range: object
    P91_has_unit: Tuple[object, ...] = ()  # Range: E58MeasurementUnit
