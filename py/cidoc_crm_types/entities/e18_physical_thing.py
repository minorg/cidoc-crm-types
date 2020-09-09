from .e72_legal_object import E72LegalObject
from dataclasses import dataclass


@dataclass
class E18PhysicalThing(E72LegalObject):
    """
Scope note:
This class comprises all persistent physical items with a relatively stable form, human-made or natural.

Depending on the existence of natural boundaries of such things, the CIDOC CRM distinguishes the instances of E19 Physical Object from instances of E26 Physical Feature, such as holes, rivers, pieces of land etc. Most instances of E19 Physical Object can be moved (if not too heavy), whereas features are integral to the surrounding matter. An instance of E18 Physical Thing occupies not only a particular geometric space at any instant of its existence, but in the course of its existence it also forms a trajectory through spacetime, which occupies a real, that is phenomenal, volume in spacetime. We include in the occupied space the space filled by the matter of the physical thing and all its inner spaces, such as the interior of a box. For the purpose of more detailed descriptions of the presence of an instance of E18 Physical Thing in space and time it can be associated with its specific instance of E92 Spacetime Volume by the property P196 defines (is defined by).

The CIDOC CRM is generally not concerned with amounts of matter in fluid or gaseous states, as long as they are not confined in an identifiable way for an identifiable minimal time-span.


Examples:
- the Cullinan Diamond (E19) (Scarratt and Shor, 2006)
- the cave &#8220;Ideon Andron&#8221; in Crete (E26) (Smith, 1844-49)
- the Mona Lisa (E22) (Mohem, 2006)


In First Order Logic:
E18(x) &#8835; E72(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E18_Physical_Thing"
