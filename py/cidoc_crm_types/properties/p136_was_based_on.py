from .p15_was_influenced_by import P15WasInfluencedBy
from dataclasses import dataclass


@dataclass
class P136WasBasedOn(P15WasInfluencedBy):
    """
Scope note:
This property identifies one or more instances of E1 CRM Entity that were used as evidence to declare a new instance of E55 Type.

The examination of these items is often the only objective way to understand the precise characteristics of a new type. Such items should be deposited in a museum or similar institution for that reason. The taxonomic role renders the specific relationship of each item to the type, such as "holotype" or "original element".


Examples:
- the taxon creation of the plant species 'Serratula glauca Linn&#233;, 1753.' (E83) was based on Object BM000576251 of the Clayton Herbarium (E20)  in the taxonomic role original element (E55)


In First Order Logic:
P136(x,y) &#8835; E83(x)
P136(x,y) &#8835; E1(y)
P136(x,y,z) &#8835; [P136(x,y) &#8743; E55(z)]
P136(x,y) &#8835; P15(x,y)
    """

    URI = "http://erlangen-crm.org/current/P136_was_based_on"
