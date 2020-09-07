from dataclasses import dataclass
from .e26_physical_feature import E26PhysicalFeature
from .e24_physical_man_made_thing import E24PhysicalManMadeThing


@dataclass
class E25ManMadeFeature(E26PhysicalFeature, E24PhysicalManMadeThing):
    pass
