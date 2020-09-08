from .e7_activity import E7Activity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E10TransferofCustody(E7Activity):
    P30_transferred_custody_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
