from .e7_activity import E7Activity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E8Acquisition(E7Activity):
    P24_transferred_title_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
