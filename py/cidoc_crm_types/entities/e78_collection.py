from .e24_physical_man_made_thing import E24PhysicalManMadeThing
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E78Collection(E24PhysicalManMadeThing):
    P147_was_curated_by: Tuple[object, ...] = ()  # Range: E87CurationActivity
