from .p12i_was_present_at import P12iWasPresentAt
from dataclasses import dataclass


@dataclass
class P11iParticipatedIn(P12iWasPresentAt):
    URI = "http://erlangen-crm.org/current/P11i_participated_in"
