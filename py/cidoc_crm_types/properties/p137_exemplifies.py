from .p2_has_type import P2HasType
from dataclasses import dataclass


@dataclass
class P137Exemplifies(P2HasType):
    """
Scope note:
This property associates an instance of E1 CRM Entity with an instance of E55 Type for which it has been declared to be a particularly characteristic example.

The P137.1 in the taxonomic role property of P137 exemplifies (is exemplified by) allows differentiation of taxonomic roles. The taxonomic role renders the specific relationship of this example to the type, such as "prototypical", "archetypical", "lectotype", etc. The taxonomic role "lectotype" is not associated with the instance of E83 Type Creation itself, but selected in a later phase.


Examples:
- Object BM000098044 of the Clayton Herbarium (E20) exemplifies Spigelia marilandica (L.) L. (E55) in the taxonomic role lectotype


In First Order Logic:
P137(x,y) &#8835; E1(x)
P137(x,y) &#8835; E55(y)
P137(x,y,z) &#8835; [P137(x,y) &#8743; E55(z)]
P137(x,y) &#8835; P2(x,y)
    """

    URI = "http://erlangen-crm.org/current/P137_exemplifies"
