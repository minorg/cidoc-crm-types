from .p11i_participated_in import P11iParticipatedIn
from dataclasses import dataclass


@dataclass
class P151iParticipatedIn(P11iParticipatedIn):
    URI = "http://erlangen-crm.org/current/P151i_participated_in"
