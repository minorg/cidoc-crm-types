from .p11_had_participant import P11HadParticipant
from dataclasses import dataclass


@dataclass
class P145Separated(P11HadParticipant):
    """
Scope note:
This property identifies the instance of E39 Actor that leaves an instance of E74 Group through an instance of E86 Leaving.


Examples:
- The end of Sir Isaac Newton's duty as Member of Parliament for the University of Cambridge to the Convention Parliament in 1702 separated Sir Isaac Newton
- George Washington's leaving office in 1797 separated George Washington
- The implementation of the treaty regulating the termination of Greenland membership in EU between EU, Denmark and Greenland February 1. 1985 (E86) separated Greenland (E74)


In First Order Logic:
P145(x,y) &#8835; E86(x)
P145(x,y) &#8835; E39(y)
P145(x,y) &#8835; P11(x,y)
    """

    URI = "http://erlangen-crm.org/current/P145_separated"
