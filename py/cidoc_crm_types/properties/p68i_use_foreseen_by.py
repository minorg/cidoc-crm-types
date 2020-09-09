from .p67i_is_referred_to_by import P67iIsReferredToBy
from dataclasses import dataclass


@dataclass
class P68iUseForeseenBy(P67iIsReferredToBy):
    URI = "http://erlangen-crm.org/current/P68i_use_foreseen_by"
