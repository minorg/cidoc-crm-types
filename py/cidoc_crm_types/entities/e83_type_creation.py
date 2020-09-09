from .e65_creation import E65Creation
from dataclasses import dataclass


@dataclass
class E83TypeCreation(E65Creation):
    """
Scope note:
This class comprises activities formally defining new types of items.

It is typically a rigorous scholarly or scientific process that ensures a type is exhaustively described and appropriately named. In some cases, particularly in archaeology and the life sciences, E83 Type Creation requires the identification of an exemplary specimen and the publication of the type definition in an appropriate scholarly forum. The activity modelled as an instance of E83 Type Creation is central to research in the life sciences, where a type would be referred to as a &#8220;taxon,&#8221; the type description as a &#8220;protologue,&#8221; and the exemplary specimens as &#8220;original element&#8221; or &#8220;holotype&#8221;.


Examples:
- creation of the taxon 'Penicillium brefeldianum B. O. Dodge' (1933)
- addition of class E85 Joining to the CIDOC CRM


In First Order Logic:
E83(x) &#8835; E65(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E83_Type_Creation"
