from dataclasses import dataclass


@dataclass
class P97FromFather:
    """
Scope note:
This property links an instance of E67 Birth to an instance of E21 Person in the role of biological father. 

Note that biological fathers are not seen as necessary participants in the birth, whereas birth-giving mothers are (see P96 by mother (gave birth)). The Person being born is linked to the Birth with the property P98 brought into life (was born).

This is not intended for use with general natural history material, only people. There is no explicit method for modelling conception and gestation except by using extensions.
An instance of E67 Birth is normally (but not always) associated with one biological father


Examples:
- King George VI (E21) was father for the birth of Queen Elizabeth II (E67)


In First Order Logic:
P97(x,y) &#8835; E67(x)
P97(x,y) &#8835; E21(y)
    """

    URI = "http://erlangen-crm.org/current/P97_from_father"
