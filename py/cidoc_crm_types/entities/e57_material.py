from .e55_type import E55Type
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E57Material(E55Type):
    """
Scope note:
This class is a specialization of E55 Type and comprises the concepts of materials.

Instances of E57 Material may denote properties of matter before its use, during its use, and as incorporated in an object, such as ultramarine powder, tempera paste, reinforced concrete. Discrete pieces of raw-materials kept in museums, such as bricks, sheets of fabric, pieces of metal, should be modelled individually in the same way as other objects. Discrete used or processed pieces, such as the stones from Nefer Titi's temple, should be modelled as parts (cf. P46 is composed of (forms part of): E18 Physical Thing).

This type is used categorically in the model without reference to instances of it, i.e. the Model does not foresee the description of instances of instances of E57 Material, e.g.: ?instances of gold?. 

It is recommended that internationally or nationally agreed codes and terminology are used.


Examples:
- Brick (Gurcke, 1987)
- Gold (Watson, 1990)
- Aluminium (Norman, 1986)
- Polycarbonate (Mhaske, 2011)
- Resin (Barton, 1992)


In First Order Logic:
E57(x) ? E55(x)
    """

    P126_was_employed_in: Tuple[object, ...] = ()  # Range: E11Modification
    P45_is_incorporated_in: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P68_use_foreseen_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    __typename: str = 'E57Material'
