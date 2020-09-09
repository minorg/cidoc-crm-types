from dataclasses import dataclass


@dataclass
class P107HasCurrentOrFormerMember:
    """
Scope note:
This property associates an instance of E74 Group with an instance of E39 Actor that is or has been a member thereof.

Instances of E74 Grous and E21 Person, may all be members of instances of E74 Group.An instance of E74 Group may be founded initially without any member.

This property is a shortcut of the more fully developed path E74 Group , P144i gained member by, E85 Joining, P143 joined , E39 Actor
The property P107.1 kind of member can be used to specify the type of membership or the role the member has in the group. 


Examples:
- Moholy Nagy (E21) is current or former member of Bauhaus (E74)
- National Museum of Science and Industry (E74) has current or former member The National Railway Museum (E74)
- The married couple Queen Elisabeth and Prince Phillip (E74) has current or former member Prince Phillip (E21) with P107.1 kind of member husband (E55 Type)


In First Order Logic:
P107(x,y) &#8835; E74(x)
P107(x,y) &#8835; E39(y)
P107(x,y,z) &#8835; [P107(x,y) &#8743; E55(z)]
    """

    URI = "http://erlangen-crm.org/current/P107_has_current_or_former_member"
