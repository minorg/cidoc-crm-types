from dataclasses import dataclass
from .e71_man_made_thing import E71ManMadeThing
from .e18_physical_thing import E18PhysicalThing

@dataclass
class E24PhysicalManMadeThing(E71ManMadeThing, E18PhysicalThing):
    pass
