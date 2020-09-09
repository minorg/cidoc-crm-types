from .p128_carries import P128Carries
from dataclasses import dataclass


@dataclass
class P65ShowsVisualItem(P128Carries):
    """
Scope note:
This property documents an instance of E36 Visual Item shown by an instance of E24 Physical Human-Made Thing.

This property is similar to P62 depicts (is depicted by) in that it associates an instance of E24 Physical Human-Made Thing with a visual representation. However, P65 shows visual item (is shown by) differs from the P62 depicts (is depicted by) property in that it makes no claims about what the instance of E36 Visual Item is deemed to represent. An instance of E36 Visual Item identifies a recognisable image or visual symbol, regardless of what this image may or may not represent.

For example, all recent British coins bear a portrait of Queen Elizabeth II, a fact that is correctly documented using P62 depicts (is depicted by). Different portraits have been used at different periods, however. P65 shows visual item (is shown by) can be used to refer to a particular portrait. P65 shows visual item (is shown by) may also be used for Visual Items such as signs, marks and symbols, for example the 'Maltese Cross' or the 'copyright symbol&#8217; that have no particular representational content. 

This property is part of the fully developed path E24 Physical Human-Made Thing , P65 shows visual item, E36 Visual Item, P138 represents,E1 CRM Entity which is shortcut by, P62 depicts (is depicted by).


Examples:
- My T-Shirt (E22) shows visual item Mona Lisa (E38)


In First Order Logic:
P65(x,y) &#8835; E24(x)
P65(x,y) &#8835; E36(y)
P65(x,y) &#8835; P128(x,y)
    """

    URI = "http://erlangen-crm.org/current/P65_shows_visual_item"
