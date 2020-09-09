from .p11_had_participant import P11HadParticipant
from dataclasses import dataclass


@dataclass
class P96ByMother(P11HadParticipant):
    """
Scope note:
This property links an instance ofE67 Birth to an instance of E21 Person in the role of birth-giving mother. Note that biological fathers are not necessarily participants in the Birth (see P97 from father (was father for)). The instance of P21 Person being born is linked to the instance of E67 Birth with the property P98 brought into life (was born). This is not intended for use with general natural history material, only people. There is no explicit method for modelling conception and gestation except by using extensions.
This is a sub-property of P11 had participant (participated in).


Examples:
- the birth of Queen Elizabeth II (E67) by mother Queen Mother (E21)


In First Order Logic:
P96(x,y) &#8835; E67(x)
P96(x,y) &#8835; E21(y)
P96(x,y) &#8835; P11(x,y)
    """

    URI = "http://erlangen-crm.org/current/P96_by_mother"
