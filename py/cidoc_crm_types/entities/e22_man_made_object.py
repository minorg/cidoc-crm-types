from .e19_physical_object import E19PhysicalObject
from .e24_physical_man_made_thing import E24PhysicalManMadeThing
from dataclasses import dataclass


@dataclass
class E22ManMadeObject(E24PhysicalManMadeThing, E19PhysicalObject):
    """
Scope note:
This class comprises physical objects purposely created by human activity.

No assumptions are made as to the extent of modification required to justify regarding an object as human-made. For example, an inscribed piece of rock or a preserved butterfly are both regarded as instances of E22 Human-Made Object.


Examples:
- Mallard (the World?s fastest steam engine) (Solomon, 2003)
- the Portland Vase (Walker, 2004)
- the Coliseum (Hopkins, 2005)


In First Order Logic:
E22(x) ? E19(x)
E22(x) ? E24(x)
    """

    _typename: str = 'E22ManMadeObject'
