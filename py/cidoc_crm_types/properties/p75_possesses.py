from dataclasses import dataclass


@dataclass
class P75Possesses:
    """
Scope note:
This property identifies former or current instances of E30 Rights held by an E39 Actor.

Examples:
- Michael Jackson (E21) possesses Intellectual property rights on the Beatles' back catalogue (E30)

In First Order Logic:
P75(x,y) &#8835; E39(x)
P75(x,y) &#8835; E30(y)
    """

    URI = "http://erlangen-crm.org/current/P75_possesses"
