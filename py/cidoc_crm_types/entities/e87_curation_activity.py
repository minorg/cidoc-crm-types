from .e7_activity import E7Activity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E87CurationActivity(E7Activity):
    P147_curated: Tuple[object, ...] = ()  # Range: E78Collection
