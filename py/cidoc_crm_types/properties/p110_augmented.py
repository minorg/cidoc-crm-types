from .p31_has_modified import P31HasModified
from dataclasses import dataclass


@dataclass
class P110Augmented(P31HasModified):
    """
Scope note:
This property identifies the instance of E24 Physical Human-Made Thing that is added to (augmented) in an instance of E79 Part Addition.

Although an instance of E79 Part Addition event normally concerns only one instance of E24 Physical Human-Made Thing, it is possible to imagine circumstances under which more than one item might be added to (augmented). For example, the artist Jackson Pollock trailing paint onto multiple canvasses.


Examples:
- the final nail-insertion Event (E79) augmented Coffin of George VI (E24)


In First Order Logic:
P110(x,y) &#8835; E79(x)
P110(x,y) &#8835; E24(y)
P110(x,y) &#8835; P31(x,y)
    """

    URI = "http://erlangen-crm.org/current/P110_augmented"
