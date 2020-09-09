from dataclasses import dataclass


@dataclass
class P157IsAtRestRelativeTo:
    """
Scope note:
This property associates an instance of E53 Place with the instance of E18 Physical Thing that determines a reference space for this instance of E53 Place by being at rest with respect to this reference space. The relative stability of form of an instance of E18 Physical Thing defines its default reference space. The reference space is not spatially limited to the referred thing. For example, a ship determines a reference space in terms of which other ships in its neighbourhood may be described. Larger constellations of matter, such as continental plates, may comprise many physical features that are at rest with them and define the same reference space. 


Examples:
- The spatial extent of the municipality of Athens in 2014 (E53) is at rest relative to The Royal Observatory in Greenwich (E25)
- The place where Lord Nelson died on H.M.S. Victory (E53) is at rest relative to H.M.S. Victory (E22)


In First Order Logic:
P157(x,y) &#8835; E53(x)
P157(x,y) &#8835; E18(y)
    """

    URI = "http://erlangen-crm.org/current/P157_is_at_rest_relative_to"
