from dataclasses import dataclass


@dataclass
class P140AssignedAttributeTo:
    """
Scope note:
This property associates an instance of E13 Attribute Assignment with the instance of E1 CRM Entity about which it made an attribution. The instance of E1 CRM Entity plays the role of the domain of the attribution.

The kind of attribution made should be documented using P177 assigned property type.


Examples:
- February 1997 Current Ownership Assessment of Martin Doerr's silver cup (E13) assigned attribute to Martin Doerr's silver cup (E19)
- 01 June 1997 Identifier Assignment of the silver cup donated by Martin Doerr (E15) assigned attribute to silver cup 232 (E19)


In First Order Logic:
P140(x,y) &#8835; E13(x)
P140(x,y) &#8835; E1(y)
    """

    URI = "http://erlangen-crm.org/current/P140_assigned_attribute_to"
