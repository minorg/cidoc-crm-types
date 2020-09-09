from dataclasses import dataclass


@dataclass
class P105RightHeldBy:
    """
Scope note:
This property identifies the instance of E39 Actor who holds the instances of E30 Right to an instance of E72 Legal Object.

It is a superproperty of P52 has current owner (is current owner of) because ownership is a right that is held on the owned object.
P105 right held by (has right on) is a shortcut of the fully developed path E72 Legal Object,P104 is subject to, E30 Right, P75i is possessed by, E39 Actor.


Examples:
- Beatles back catalogue (E73) right held by Michael Jackson (E21)


In First Order Logic:
P105(x,y) &#8835; E72(x)
P105(x,y) &#8835; E39(y)
    """

    URI = "http://erlangen-crm.org/current/P105_right_held_by"
