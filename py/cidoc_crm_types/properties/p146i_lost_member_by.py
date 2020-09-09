from .p11i_participated_in import P11iParticipatedIn
from dataclasses import dataclass


@dataclass
class P146iLostMemberBy(P11iParticipatedIn):
    URI = "http://erlangen-crm.org/current/P146i_lost_member_by"
