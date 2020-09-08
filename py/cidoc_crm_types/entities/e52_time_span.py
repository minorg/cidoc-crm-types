from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E52TimeSpan(E1CRMEntity):
    P160i_is_temporal_projection_of: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P164i_was_time_span_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P170i_time_is_defined_by: Tuple[object, ...] = ()  # Range: object
    P191_had_duration: Tuple[object, ...] = ()  # Range: E54Dimension
    P4_is_time_span_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P79_beginning_is_qualified_by: Tuple[object, ...] = ()  # Range: object
    P80_end_is_qualified_by: Tuple[object, ...] = ()  # Range: object
    P81_ongoing_throughout: Tuple[object, ...] = ()  # Range: object
    P82_at_some_time_within: Tuple[object, ...] = ()  # Range: object
    P86_contains: Tuple[object, ...] = ()  # Range: E52TimeSpan
    P86_falls_within: Tuple[object, ...] = ()  # Range: E52TimeSpan
