from .e2_temporal_entity import E2TemporalEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E3ConditionState(E2TemporalEntity):
    P35_was_identified_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P44_is_condition_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P5_consists_of: Tuple[object, ...] = ()  # Range: E3ConditionState
    P5_forms_part_of: Tuple[object, ...] = ()  # Range: E3ConditionState
