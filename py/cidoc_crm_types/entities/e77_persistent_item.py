from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E77PersistentItem(E1CRMEntity):
    P12_was_present_at: Tuple[object, ...] = ()  # Range: E5Event
    P92_was_brought_into_existence_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P93_was_taken_out_of_existence_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
