from .p11_had_participant import P11HadParticipant
from dataclasses import dataclass


@dataclass
class P143Joined(P11HadParticipant):
    """
Scope note:
This property identifies the instance of E39 Actor that becomes member of an instance of E74 Group in an instance of E85 Joining.

Joining events allow for describing people becoming members of a group with the more detailed path E74 Group, P144i gained member by, E85 Joining, P143 joined , E39 Actor, compared to the shortcut offered by P107 has current or former member (is current or former member of).


Examples:
- The election of Sir Isaac Newton as Member of Parliament to the Convention Parliament of 1689 (E85) joined Sir Isaac Newton (E21)
- The inauguration of Mikhail Sergeyevich Gorbachev as leader of the Union of Soviet Socialist Republics (USSR) in 1985 (E85) joined Mikhail Sergeyevich Gorbachev (E21)
- The implementation of the membership treaty January 1. 1973 between EU and Denmark (E85) joined Denmark (E74)


In First Order Logic:
P143(x,y) &#8835; E85(x)
P143(x,y) &#8835; E39(y)
P143(x,y) &#8835; P11(x,y)
    """

    URI = "http://erlangen-crm.org/current/P143_joined"
