from .p11_had_participant import P11HadParticipant
from dataclasses import dataclass


@dataclass
class P146SeparatedFrom(P11HadParticipant):
    """
Scope note:
This property identifies the instance of E74 Group an instance of E39 Actor leaves through an instance of E86 Leaving.

Although a Leaving activity normally concerns only one instance of E74 Group, it is possible to imagine circumstances under which leaving one E74 Group implies leaving another E74 Group as well.


Examples:
- The end of Sir Isaac Newton's duty as Member of Parliament for the University of Cambridge to the Convention Parliament in 1702 separated from the Convention Parliament
- George Washington's leaving office in 1797 separated from the office of President of the United States
- The implementation of the treaty regulating the termination of Greenland membership in EU between EU, Denmark and Greenland February 1. 1985 separated from EU (E74)


In First Order Logic:
P146(x,y) &#8835; E86(x)
P146(x,y) &#8835; E74(y)
P146(x,y) &#8835; P11(x,y)
    """

    URI = "http://erlangen-crm.org/current/P146_separated_from"
