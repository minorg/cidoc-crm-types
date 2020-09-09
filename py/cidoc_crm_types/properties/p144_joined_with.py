from .p11_had_participant import P11HadParticipant
from dataclasses import dataclass


@dataclass
class P144JoinedWith(P11HadParticipant):
    """
Scope note:
This property identifies the instance of E74 Group of which an instance of E39 Actor becomes a member through an instance of E85 Joining.

Although a Joining activity normally concerns only one instance of E74 Group, it is possible to imagine circumstances under which becoming member of one Group implies becoming member of another Group as well.

Joining events allow for describing people becoming members of a group with a more detailed path from E74 Group through, P144i gained member by, E85 Joining, P143 joined , E39 Actor, compared to the shortcut offered by P107 has current or former member (is current or former member of). The property P144.1 kind of member can be used to specify the type of membership or the role the member has in the group.


Examples:
- The election of Sir Isaac Newton as Member of Parliament to the Convention Parliament of 1689 (E85) joined with the Convention Parliament (E74)
- The inauguration of Mikhail Sergeyevich Gorbachev as Leader of the Union of Soviet Socialist Republics (USSR) in 1985 (E85) joined with the office of Leader of the Union of Soviet Socialist Republics (USSR) (E74) with P144.1 kind  of member President (E55)
- The implementation of the membership treaty January 1. 1973 between EU and Denmark (E85) joined with EU (E74)


In First Order Logic:
P144(x,y) &#8835; E85(x)
P144(x,y)&#8835; E74(y)
P144(x,y,z) &#8835; [P144(x,y) &#8743; E55(z)]
P144(x,y) &#8835; P11(x,y)
    """

    URI = "http://erlangen-crm.org/current/P144_joined_with"
