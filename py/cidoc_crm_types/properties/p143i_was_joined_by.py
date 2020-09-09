from .p11i_participated_in import P11iParticipatedIn
from dataclasses import dataclass


@dataclass
class P143iWasJoinedBy(P11iParticipatedIn):
    URI = "http://erlangen-crm.org/current/P143i_was_joined_by"
