from .p15_was_influenced_by import P15WasInfluencedBy
from .p174_starts_before_the_end_of import P174StartsBeforeTheEndOf
from dataclasses import dataclass


@dataclass
class P134Continued(P15WasInfluencedBy, P174StartsBeforeTheEndOf):
    """
Scope note:
This property associates two instances of E7 Activity, where the domain is considered as an intentional continuation of the range. A continuation of an activity may happen when the continued activity is still ongoing or after the continued activity has completely ended. The continuing activity may have started already before it decided to continue the other one. Continuation implies a coherence of intentions and outcomes of the involved activities.


Examples:
- the construction of the K&#246;lner Dom (Cologne Cathedral) (E7), abandoned in the 15th century, was continued by construction in the 19th century adapting the initial plans so as to preserve the intended appearance (E7)


In First Order Logic:
P134(x,y) &#8835; E7(x)
P134(x,y)&#8835; E7(y)
P134(x,y) &#8835; P15(x,y)
P134(x,y) &#8835; P174(x,y)
    """

    URI = "http://erlangen-crm.org/current/P134_continued"
