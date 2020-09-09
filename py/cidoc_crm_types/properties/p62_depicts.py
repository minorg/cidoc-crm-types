from dataclasses import dataclass


@dataclass
class P62Depicts:
    """
Scope note:
This property identifies something that is depicted by an instance of E24 Physical Human-Made Thing.
Depicting is meant in the sense that an instance of E24 Physical Human-Made Thing intentionally shows, through its optical qualities or form, a representation of the entity depicted. Photographs are by default regarded as being intentional in this sense. Anything that is designed to change the properties of the depiction, such as an e-book reader, is specifically excluded. The property does not pertain to inscriptions or any other information encoding.

This property is a shortcut of the more fully developed path from E24 Physical Human-Made Thing through P65 shows visual item, E36 Visual Item, P138 represents, E1 CRM Entity. P138.1 mode of representation &#8220;depiction&#8221; allows the nature of the depiction to be refined.


Examples:
- The painting "La Libert&#233; guidant le peuple" by Eug&#232;ne Delacroix (E22) depicts the French "July Revolution" of 1830 (E7)
- the 20 pence coin held by the Department of Coins and Medals of the British Museum under registration number 2006,1101.126 (E24) depicts Queen Elizabeth II (E21) mode of depiction Profile (E55)


In First Order Logic:
P62(x,y) &#8835; E24(x)
P62(x,y) &#8835; E1(y)
P62(x,y,z) &#8835; [P62(x,y) &#8743; E55(z)]

Properties: P62.1 mode of depiction: E55 Type
    """

    URI = "http://erlangen-crm.org/current/P62_depicts"
