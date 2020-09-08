from .e24_physical_man_made_thing import E24PhysicalManMadeThing
from .e26_physical_feature import E26PhysicalFeature
from dataclasses import dataclass


@dataclass
class E25ManMadeFeature(E24PhysicalManMadeThing, E26PhysicalFeature):

