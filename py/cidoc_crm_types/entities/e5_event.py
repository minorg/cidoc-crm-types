from .e4_period import E4Period
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E5Event(E4Period):
    P11_had_participant: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P12_occurred_in_the_presence_of: Tuple[object, ...] = ()  # Range: E77PersistentItem
    P20_was_purpose_of: Tuple[object, ...] = ()  # Range: E7Activity
