from .e70_thing import E70Thing
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E71ManMadeThing(E70Thing):
    """
Scope note:
This class comprises discrete, identifiable human-made items that are documented as single units.

These items are either intellectual products or human-made physical things, and are characterized by relative stability. They may for instance have a solid physical form, an electronic encoding, or they may be logical concepts or structures. 


Examples:
- Beethoven?s 5th Symphony (E73) (Lockwood, 2015)
- Michelangelo?s David (Paoletti, 2015)
- Einstein?s Theory of General Relativity (E73) (Hartle, 2003)
- the taxon ?Fringilla coelebs Linnaeus,1758? (E55) (Sinkevicius and Narusevicius, 2002)


In First Order Logic:
E71(x) ? E70(x)
    """

    P102_has_title: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P103_was_intended_for: Tuple[object, ...] = ()  # Range: E55Type
    P19_was_made_for: Tuple[object, ...] = ()  # Range: E7Activity
