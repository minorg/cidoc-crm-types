from dataclasses import dataclass


@dataclass
class P125UsedObjectOfType:
    """
Scope note:
This property associates an instance of E7 Activity to an instance of E55 Type,which defines used in an instance of E7 Activity, when the specific instance is either unknown or not of interest, such as use of "a hammer".


Examples:
- at the Battle of Agincourt (E7), the English archers used object of type long bow (E55)


In First Order Logic:
P125(x,y) &#8835; E7(x)
P125(x,y) &#8835; E55(y)
P125(x,y) iff (&#8707;z)[E70(z) &#8743; P16(x,z) &#8743; P2(z,y)]
    """

    URI = "http://erlangen-crm.org/current/P125_used_object_of_type"
