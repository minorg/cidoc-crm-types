from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E2TemporalEntity(E1CRMEntity):
    P173_starts_before_or_at_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P174_ends_after_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P174_starts_before_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P175_starts_before_or_with_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P175i_starts_after_or_with_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P176_starts_before_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P176i_starts_after_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P182_ends_befort_or_at_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P182i_starts_after_or_with_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P183_ends_before_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P183i_starts_after_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P184_ends_before_or_with_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P184_ens_before_or_with_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P185_ends_before_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P185i_ends_after_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P4_has_time_span: Tuple[object, ...] = ()  # Range: E52TimeSpan
