from dataclasses import dataclass


@dataclass
class P127HasBroaderTerm:
    """
Scope note:
This property associates an instance of E55 Type with another instance of E55 Type that has a broader meaning.

It allows instances of E55 Types to be organised into hierarchies. This is the sense of "broader term generic (BTG)" as defined in ISO 25964-2:2013.

This property is transitive.


Examples:
- dime (E55) has broader term coin (E55)


In First Order Logic:
P127(x,y) &#8835; E55(x)
P127(x,y) &#8835; E55(y)
    """

    URI = "http://erlangen-crm.org/current/P127_has_broader_term"
