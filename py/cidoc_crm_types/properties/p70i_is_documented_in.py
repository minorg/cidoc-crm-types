from .p67i_is_referred_to_by import P67iIsReferredToBy
from dataclasses import dataclass


@dataclass
class P70iIsDocumentedIn(P67iIsReferredToBy):
    URI = "http://erlangen-crm.org/current/P70i_is_documented_in"
