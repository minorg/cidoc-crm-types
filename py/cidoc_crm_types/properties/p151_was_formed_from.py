from .p11_had_participant import P11HadParticipant
from dataclasses import dataclass


@dataclass
class P151WasFormedFrom(P11HadParticipant):
    """
Scope note:
This property associates an instance of E66 Formation with an instance of E74 Group from which the new group was formed preserving a sense of continuity such as in mission, membership or tradition.


Examples:
- The formation of the House of Bourbon-Conti in 1581 (E66) was formed from House of Cond&#233; (E74)


In First Order Logic:
P151(x,y) &#8835; E66(x)
P151(x,y) &#8835; E74(y)
P151(x,y) &#8835; P11(x,y)
    """

    URI = "http://erlangen-crm.org/current/P151_was_formed_from"
