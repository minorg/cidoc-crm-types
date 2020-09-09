from .p1_is_identified_by import P1IsIdentifiedBy
from dataclasses import dataclass


@dataclass
class P102HasTitle(P1IsIdentifiedBy):
    """
Scope note:
This property associates an instance of E35 Title has been applied to an instance of E71 Human-Made Thing.

The P102.1 has type property of the P102 has title (is title of) property enables the relationship between the title and the thing to be further clarified, for example, if the title was a given title, a supplied title etc. 
It allows any human-made material or immaterial thing to be given a title. It is possible to imagine a title being created without a specific object in mind.


Examples:
- the first book of the Old Testament (E33) has title "Genesis" (E35) has type translated (E55)


In First Order Logic:
P102(x,y) &#8835; E71(x)
P102(x,y) &#8835; E35(y)
P102(x,y,z) &#8835; [P102(x,y) &#8743; E55(z)]
P102(x,y) &#8835; P1(x,y)
    """

    URI = "http://erlangen-crm.org/current/P102_has_title"
