from .p12_occurred_in_the_presence_of import P12OccurredInThePresenceOf
from dataclasses import dataclass


@dataclass
class P92BroughtIntoExistence(P12OccurredInThePresenceOf):
    """
Scope note:
This property links an instance of E63 Beginning of Existence to the instance of E77 Persistent Item brought into existence by it.

It allows a &#8220;start&#8221; to be attached to any instance of E77 Persistent Item being documented, i.e. as instances of E70 Thing, E72 Legal Object, E39 Actor, E41 Appellation and E55 Type.


Examples:
- the birth of Mozart (E67) brought into existence Mozart (E21)


In First Order Logic:
P92(x,y) &#8835; E63(x)
P92(x,y) &#8835; E77(y)
P92(x,y) &#8835; P12(x,y)
    """

    URI = "http://erlangen-crm.org/current/P92_brought_into_existence"
