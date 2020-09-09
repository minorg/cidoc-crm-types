from dataclasses import dataclass


@dataclass
class P141Assigned:
    """
Scope note:
This property associates an instance of E13 Attribute Assignment with the instance of E1 CRM Entity used in the attribution. The instance of E1 CRM Entity here plays the role of the range of the attribution.

The kind of attribution made should be documented using P177 assigned property type.


Examples:
- February 1997 Current Ownership Assessment of Martin Doerr's silver cup (E13) assigned Martin Doerr (E21)
- 01 June 1997 Identifier Assignment of the silver cup donated by Martin Doerr (E15) assigned object identifier 232


In First Order Logic:
P141(x,y) &#8835; E13(x)
P141(x,y) &#8835; E1(y)
    """

    URI = "http://erlangen-crm.org/current/P141_assigned"
