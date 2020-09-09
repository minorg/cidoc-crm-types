from .e5_event import E5Event
from dataclasses import dataclass


@dataclass
class E63BeginningofExistence(E5Event):
    """
Scope note:
This class comprises events that bring into existence any instance of E77 Persistent Item.

It may be used for temporal reasoning about things (intellectual products, physical items, groups of people, living beings) beginning to exist; it serves as a hook for determination of a &#8220;terminus post quem&#8221; or &#8220;terminus ante quem&#8221;. 


Examples:
- the birth of my child
- the birth of Snoopy, my dog
- the calving of the iceberg that sank the Titanic
- the construction of the Eiffel Tower (Tissandier, 1889)


In First Order Logic:
E63(x) &#8835; E5(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E63_Beginning_of_Existence"
