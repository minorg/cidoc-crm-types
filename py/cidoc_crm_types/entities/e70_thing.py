from .e77_persistent_item import E77PersistentItem
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E70Thing(E77PersistentItem):
    """
Scope note:
This general class comprises discrete, identifiable, instances of E77 Persistent Item that are documented as single units, that either consist of matter or depend on being carried by matter and are characterized by relative stability.

They may be intellectual products or physical things. They may for instance have a solid physical form, an electronic encoding, or they may be a logical concept or structure.


Examples:
- my photograph collection (E78)
- the bottle of milk in my refrigerator (E22)
- the Riss A1 plan of the Stra?burger M?nster (French: Cath?drale Notre-Dame de Strasbourg) (E29) (Liess, R., 1985)
- the thing on the top of Otto Hahn?s desk (E19)
- the form of the no-smoking sign (E36)
- the cave of Dirou, Mani, Greece (E27) (Psimenos. 2005)


In First Order Logic:
E70(x) ? E77(x)
    """

    P101_had_as_general_use: Tuple[object, ...] = ()  # Range: E55Type
    P130_features_are_also_found_on: Tuple[object, ...] = ()  # Range: E70Thing
    P130_shows_features_of: Tuple[object, ...] = ()  # Range: E70Thing
    P43_has_dimension: Tuple[object, ...] = ()  # Range: E54Dimension
    __typename: str = 'E70Thing'
