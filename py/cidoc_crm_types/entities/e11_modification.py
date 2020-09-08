from .e7_activity import E7Activity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E11Modification(E7Activity):
    """
Scope note:
This class comprises instances of E7 Activity that create, alter or change instances of E24 Physical Human-Made Thing.

This class includes the production of an item from raw materials, and other so far undocumented objects, and the preventive treatment or restoration of an object for conservation.

Since the distinction between modification and production is not always clear, modification is regarded as the more generally applicable concept. This implies that some items may be consumed or destroyed in an instance of E11 Modification, and that others may be produced as a result of it. An event should also be documented using an instance of E81 Transformation if it results in the destruction of one or more objects and the simultaneous production of others using parts or material from the originals. In this case, the new items have separate identities.

If the instance of E29 Design or Procedure utilized for the modification prescribes the use of specific materials, they should be documented using property P68 foresees use of (use foreseen by): E57 Material of E29 Design or Procedure, rather than via P126 employed (was employed in): E57 Material.


Examples:
- the construction of the SS Great Britain (E12)(Gregor, 1971)
- the impregnation of the Vasa warship in Stockholm for preservation after 1956(H?fors, 2010)
- the transformation of the Enola Gay into a museum exhibit by the National Air and Space Museum in Washington DC between 1993 and 1995 (E12, E81) (Yakel, 2000)
- the last renewal of the gold coating of the Toshogu shrine in Nikko, Japan(Cali and Dougil, 2012)


In First Order Logic:
E11(x) ? E7(x)
    """

    P126_employed: Tuple[object, ...] = ()  # Range: E57Material
