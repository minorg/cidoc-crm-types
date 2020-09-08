from .e18_physical_thing import E18PhysicalThing
from .e71_man_made_thing import E71ManMadeThing
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E24PhysicalManMadeThing(E71ManMadeThing, E18PhysicalThing):
    P62_depicts: Tuple[object, ...] = ()  # Range: E1CRMEntity
