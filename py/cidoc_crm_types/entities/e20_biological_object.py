from .e19_physical_object import E19PhysicalObject
from dataclasses import dataclass


@dataclass
class E20BiologicalObject(E19PhysicalObject):
    """
Scope note:
This class comprises individual items of a material nature, which live, have lived or are natural products of or from living organisms.

Artificial objects that incorporate biological elements, such as Victorian butterfly frames, can be documented as both instances of E20 Biological Object and E22 Human-Made Object. 


Examples:
- me
- Tut-Ankh-Amun (Edwards, 1979)
- Boukephalas [Horse of Alexander the Great](Lamb, 2005)
- petrified dinosaur excrement PA1906-344


In First Order Logic:
E20(x) ? E19(x)
    """

    __typename: str = 'E20BiologicalObject'
