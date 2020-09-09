from dataclasses import dataclass


@dataclass
class P15WasInfluencedBy:
    """
Scope note:
This is a high level property, which captures the relationship between an E7 Activity and anything that may have had some bearing upon it.

The property has more specific sub properties.


Examples:
- the designing of the Sydney Harbour Bridge (E7) was influenced by the Tyne bridge (E22)


In First Order Logic: 
P15 (x,y) &#8835; E7(x)
P15 (x,y) &#8835; E1(y)
    """

    URI = "http://erlangen-crm.org/current/P15_was_influenced_by"
