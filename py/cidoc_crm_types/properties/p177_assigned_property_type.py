from .p2_has_type import P2HasType
from dataclasses import dataclass


@dataclass
class P177AssignedPropertyType(P2HasType):
    """
Scope note:
This property associates an instance of E13 Attribute Assignment with the type of property or relation that this assignment maintains to hold between the item to which it assigns an attribute and the attribute itself.
Note that the properties defined by the CIDOC CRM also constitute instances of E55 Type themselves. The direction of the assigned property type is understood to be from the attributed item (the range of property P140 assigned attribute to) to the attribute item (the range of the property P141 assigned). More than one property type may be assigned to hold between two items.
A comprehensive explanation about refining CIDOC CRM concepts by E55 Type is given in the section &#8220;About Types&#8221; in the section on &#8220;Specific Modelling Constructs&#8221; of this document.


Examples:
- February 1997 Current Ownership Assessment of Martin Doerr&#8217;s silver cup (E13) assigned property type P52 has former or current owner (is former or current keeper of) (E55)
- 01 June 1997 Identifier Assignment of the silver cup donated by Martin Doerr (E15) assigned property type P48 has preferred identifier (is preferred identifier of) (E55)


In First Order Logic:
 P177(x,y) &#8835; E13(x)
 P177(x,y) &#8835; E55(y)
    """

    URI = "http://erlangen-crm.org/current/P177_assigned_property_type"
