from .e18_physical_thing import E18PhysicalThing
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E19PhysicalObject(E18PhysicalThing):
    """
Scope note:
This class comprises items of a material nature that are units for documentation and have physical boundaries that separate them completely in an objective way from other objects.

The class also includes all aggregates of objects made for functional purposes of whatever kind, independent of physical coherence, such as a set of chessmen. Typically, instances of E19 Physical Object can be moved (if not too heavy).

In some contexts, such objects, except for aggregates, are also called ?bona fide objects? (Smith & Varzi, 2000, pp.401-420), i.e. naturally defined objects.

The decision as to what is documented as a complete item, rather than by its parts or components, may be a purely administrative decision or may be a result of the order in which the item was acquired.


Examples: 
- John SmithAphrodite of Milos (Kousser, 2005)
- the Palace of Knossos (Evans, 1921-36)
- the Cullinan Diamond (Scarratt and Shor, 2006)
- Apollo 13 at the time of launch (Lovell and Kluger, 1994)


In First Order Logic:
E19(x) ? E18(x)
    """

    P188i_is_production_tool_for: Tuple[object, ...] = ()  # Range: E99ProductType
    P54_has_current_permanent_location: Tuple[object, ...] = ()  # Range: E53Place
    P57_has_number_of_parts: Tuple[object, ...] = ()  # Range: object
    __typename: str = 'E19PhysicalObject'
