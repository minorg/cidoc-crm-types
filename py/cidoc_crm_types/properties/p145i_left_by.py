from .p11i_participated_in import P11iParticipatedIn
from dataclasses import dataclass


@dataclass
class P145iLeftBy(P11iParticipatedIn):
    URI = "http://erlangen-crm.org/current/P145i_left_by"
