from .p12_occurred_in_the_presence_of import P12OccurredInThePresenceOf
from dataclasses import dataclass


@dataclass
class P93TookOutOfExistence(P12OccurredInThePresenceOf):
    """
Scope note:
This property links an instance of E64 End of Existence to the instance E77 Persistent Item taken out of existence by it.

In the case of immaterial things, the instance of E64 End of Existence is considered to take place with the destruction of the last physical carrier.
This allows an &#8220;end&#8221; to be attached to any instance of E77 Persistent Item being documented i.e. instances of E70 Thing, E72 Legal Object, E39 Actor, E41 Appellation and E55 Type. For many instances of E77 Persistent Item we know the maximum life-span and can infer, that they must have ended to exist. We assume in that case an instance of E64 End of Existence, which may be as unnoticeable as forgetting the secret knowledge by the last representative of some indigenous nation.


Examples:
- the death of Mozart (E69) took out of existence Mozart (E21)


In First Order Logic:
P93 (x,y) &#8835; E64(x)
P93 (x,y) &#8835; E77(y)
P93(x,y) &#8835; P12(x,y)
    """

    URI = "http://erlangen-crm.org/current/P93_took_out_of_existence"
