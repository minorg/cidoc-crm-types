from dataclasses import dataclass


@dataclass
class P167At:
    """
Scope Note:      
This property associates an instance of E93 Presence with an instance of E53 Place that geometrically includes the spatial projection of the respective instance of E93 Presence. Besides others, this property may be used to state in which space an object has been for some known time, such as a room of a castle or in a drawer. It may also be used to describe a confinement of the spatial extent of some realm during a known time-span. It is a shortcut of the more fully developed path from E93 Presence through P161 has spatial projection, E53 Place, P89 falls within (contains) to E53 Place. 


In First Order Logic:
P167(x,y) &#8835; E93(x)
P167(x,y) &#8835; E53(y)
P167(x,y) &#8835; (&#8707;z)[ E53(z) &#8743; P161(x,z) &#8743; P89(z,y)]
    """

    URI = "http://erlangen-crm.org/current/P167_at"
