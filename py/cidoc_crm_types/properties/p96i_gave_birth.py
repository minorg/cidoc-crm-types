from .p11i_participated_in import P11iParticipatedIn
from dataclasses import dataclass


@dataclass
class P96iGaveBirth(P11iParticipatedIn):
    URI = "http://erlangen-crm.org/current/P96i_gave_birth"
