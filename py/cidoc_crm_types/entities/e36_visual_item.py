from .e73_information_object import E73InformationObject
from dataclasses import dataclass


@dataclass
class E36VisualItem(E73InformationObject):
    """
Scope note:
This class comprises the intellectual or conceptual aspects of recognisable marks and images.

This class does not intend to describe the idiosyncratic characteristics of an individual physical embodiment of a visual item, but the underlying prototype. For example, a mark such as the ICOM logo is generally considered to be the same logo when used on any number of publications. The size, orientation and colour may change, but the logo remains uniquely identifiable. The same is true of images that are reproduced many times. This means that visual items are independent of their physical support.

The class E36 Visual Item provides a means of identifying and linking together instances of E24 Physical Human-Made Thing that carry the same visual symbols, marks or images etc. The property P62 depicts (is depicted by) between E24 Physical Human-Made Thing and depicted subjects (E1 CRM Entity) is a shortcut of the more fully developed path from E24 Physical Human-Made Thing through P65 shows visual item (is shown by), E36 Visual Item, P138 represents (has representation) to E1CRM Entity, which in addition captures the optical features of the depiction.


Examples:
- the visual appearance of Monet's "La Pie"
- the Coca-Cola logo (E34)
- the Chi-Rho (E37)
- the communist red star (E37)


In First Order Logic:
E36(x) ? E73(x)
    """


