from .p12i_was_present_at import P12iWasPresentAt
from .p15i_influenced import P15iInfluenced
from dataclasses import dataclass


@dataclass
class P16iWasUsedFor(P15iInfluenced, P12iWasPresentAt):
    URI = "http://erlangen-crm.org/current/P16i_was_used_for"
