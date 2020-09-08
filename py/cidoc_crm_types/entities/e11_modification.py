from .e7_activity import E7Activity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E11Modification(E7Activity):
    P126_employed: Tuple[object, ...] = ()  # Range: E57Material
