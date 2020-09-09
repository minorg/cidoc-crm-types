from .p92_brought_into_existence import P92BroughtIntoExistence
from dataclasses import dataclass


@dataclass
class P94HasCreated(P92BroughtIntoExistence):
    """
Scope note:
This property links an instance of E65 Creation to the instance of E28 Conceptual Object created by it.

It represents the act of conceiving the intellectual content of the instance of E28 Conceptual Object. It does not represent the act of creating the first physical carrier of the instanced of E28 Conceptual Object.
As an example, this is the composition of a poem, not its commitment to paper.


Examples:
- the composition of "The Four Friends" by A. A. Milne (E65) has created "The Four Friends" by A. A. Milne (E28)


In First Order Logic:
P94(x,y) &#8835; E65(x)
P94(x,y) &#8835; E28(y)
P94(x,y) &#8835; P92(x,y)
    """

    URI = "http://erlangen-crm.org/current/P94_has_created"
