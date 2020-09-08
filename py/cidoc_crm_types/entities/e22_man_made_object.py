from .e19_physical_object import E19PhysicalObject
from .e24_physical_man_made_thing import E24PhysicalManMadeThing
from dataclasses import dataclass


@dataclass
class E22ManMadeObject(E24PhysicalManMadeThing, E19PhysicalObject):

