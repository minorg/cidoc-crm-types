from .e70_thing import E70Thing
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E72LegalObject(E70Thing):
    P104_is_subject_to: Tuple[object, ...] = ()  # Range: E30Right
    P105_right_held_by: Tuple[object, ...] = ()  # Range: E39Actor
