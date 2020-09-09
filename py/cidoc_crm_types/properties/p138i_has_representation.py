from .p67i_is_referred_to_by import P67iIsReferredToBy
from dataclasses import dataclass


@dataclass
class P138iHasRepresentation(P67iIsReferredToBy):
    URI = "http://erlangen-crm.org/current/P138i_has_representation"
