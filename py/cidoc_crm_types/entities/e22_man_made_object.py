from dataclasses import dataclass
from .e24_physical_man_made_thing import E24PhysicalManMadeThing
from .e19_physical_object import E19PhysicalObject

@dataclass
class E22ManMadeObject(E24PhysicalManMadeThing, E19PhysicalObject):
    pass
