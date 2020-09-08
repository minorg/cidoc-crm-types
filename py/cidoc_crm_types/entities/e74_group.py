from .e39_actor import E39Actor
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E74Group(E39Actor):
    P107_has_current_or_former_member: Tuple[object, ...] = ()  # Range: E39Actor
