from .p141_assigned import P141Assigned
from dataclasses import dataclass


@dataclass
class P38Deassigned(P141Assigned):
    """
Scope note:
This property records the identifier that was deassigned from an instance of E1 CRM Entity.
Deassignment of an identifier may be necessary when an item is taken out of an inventory, a new numbering system is introduced or items are merged or split up.
The same identifier may be deassigned on more than one occasion


Examples:
- 31 July 2001 Identifier Assignment of the silver cup OXCMS:2001.1.32 (E15) deassigned "232" (E42)


In First Order Logic:
P38(x,y) &#8835; E15(x)
P38(x,y) &#8835; E42(y)
P38(x,y) &#8835; P141(x,y)
    """

    URI = "http://erlangen-crm.org/current/P38_deassigned"
