from .e7_activity import E7Activity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E9Move(E7Activity):
    P26_moved_to: Tuple[object, ...] = ()  # Range: E53Place
    P27_moved_from: Tuple[object, ...] = ()  # Range: E53Place
