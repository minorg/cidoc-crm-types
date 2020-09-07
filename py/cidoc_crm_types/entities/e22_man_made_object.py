from dataclasses import dataclass
from .e19_physical_object import E19PhysicalObject
from .e24_physical_man_made_thing import E24PhysicalManMadeThing


@dataclass
class E22ManMadeObject(E19PhysicalObject, E24PhysicalManMadeThing):
    pass
