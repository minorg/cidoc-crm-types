
from dataclasses import dataclass
from .e39_actor import E39Actor
from .e20_biological_object import E20BiologicalObject

@dataclass
class E21Person(E39Actor, E20BiologicalObject):
    pass
