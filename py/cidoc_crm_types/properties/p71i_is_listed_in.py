from .p67i_is_referred_to_by import P67iIsReferredToBy
from dataclasses import dataclass


@dataclass
class P71iIsListedIn(P67iIsReferredToBy):
    URI = "http://erlangen-crm.org/current/P71i_is_listed_in"
