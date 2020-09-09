from .e70_thing import E70Thing
from dataclasses import dataclass


@dataclass
class E71HumanMadeThing(E70Thing):
    """
Scope note:
This class comprises discrete, identifiable human-made items that are documented as single units.

These items are either intellectual products or human-made physical things, and are characterized by relative stability. They may for instance have a solid physical form, an electronic encoding, or they may be logical concepts or structures. 


Examples:
- Beethoven&#8217;s 5th Symphony (E73) (Lockwood, 2015)
- Michelangelo&#8217;s David (Paoletti, 2015)
- Einstein&#8217;s Theory of General Relativity (E73) (Hartle, 2003)
- the taxon &#8216;Fringilla coelebs Linnaeus,1758&#8217; (E55) (Sinkevicius and Narusevicius, 2002)


In First Order Logic:
E71(x) &#8835; E70(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E71_Human-Made_Thing"
