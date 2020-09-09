from .e77_persistent_item import E77PersistentItem
from dataclasses import dataclass


@dataclass
class E70Thing(E77PersistentItem):
    """
Scope note:
This general class comprises discrete, identifiable, instances of E77 Persistent Item that are documented as single units, that either consist of matter or depend on being carried by matter and are characterized by relative stability.

They may be intellectual products or physical things. They may for instance have a solid physical form, an electronic encoding, or they may be a logical concept or structure.


Examples:
- my photograph collection (E78)
- the bottle of milk in my refrigerator (E22)
- the Riss A1 plan of the Stra&#223;burger M&#252;nster (French: Cath&#233;drale Notre-Dame de Strasbourg) (E29) (Liess, R., 1985)
- the thing on the top of Otto Hahn&#8217;s desk (E19)
- the form of the no-smoking sign (E36)
- the cave of Dirou, Mani, Greece (E27) (Psimenos. 2005)


In First Order Logic:
E70(x) &#8835; E77(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E70_Thing"
