from .p49_has_former_or_current_keeper import P49HasFormerOrCurrentKeeper
from dataclasses import dataclass


@dataclass
class P109HasCurrentOrFormerCurator(P49HasFormerOrCurrentKeeper):
    """
Scope note:
This property identifies the instance of E39 Actor who assumed or have assumed overall curatorial responsibility for an instance of E78 Collection.

It does not allow a history of curation to be recorded. This would require use of an event initiating a curator being responsible for a collection.


Examples:
- the Robert Opie Collection (E78) has current or former curator Robert Opie (E39)
- the Mikael Heggelund Foslie's coralline red algae Herbarium (E78) has current or former curator Mikael Heggelund Foslie


In First Order Logic:
P109(x,y) &#8835; E78(x)
P109(x,y) &#8835; E39(y)
P109(x,y) &#8835; P49(x,y)
    """

    URI = "http://erlangen-crm.org/current/P109_has_current_or_former_curator"
