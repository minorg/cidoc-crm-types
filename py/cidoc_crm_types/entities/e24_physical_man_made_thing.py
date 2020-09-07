from dataclasses import dataclass
from .e18_physical_thing import E18PhysicalThing
from .e71_man_made_thing import E71ManMadeThing


@dataclass
class E24PhysicalManMadeThing(E18PhysicalThing, E71ManMadeThing):
    pass
