from .p157i_provides_reference_space_for import P157iProvidesReferenceSpaceFor
from dataclasses import dataclass


@dataclass
class P59HasSection(P157iProvidesReferenceSpaceFor):
    """
Scope note:
This property links an area, i.e., an instance of E53 Place to the instance of E18 Physical Thing upon
which it is found. This area may either be identified by a name, or by a geometry in terms of a coordinate
system adapted to the shape of the respective instance of E18 Physical Thing. Typically, names identifying
sections of physical objects are composed of the name of a kind of part and the name of the object itself,
such as "The poop deck of H.M.S. Victory", which is composed of "poop deck" and "H.M.S. Victory".


Examples:
- HMS Victory (E22) has section HMS Victory section B347.6 (E53)


In First Order Logic:
P59(x,y) &#8835; E18(x)
P59(x,y) &#8835; E53(y)
    """

    URI = "http://erlangen-crm.org/current/P59_has_section"
