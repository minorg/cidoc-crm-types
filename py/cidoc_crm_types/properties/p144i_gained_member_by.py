from .p11i_participated_in import P11iParticipatedIn
from dataclasses import dataclass


@dataclass
class P144iGainedMemberBy(P11iParticipatedIn):
    URI = "http://erlangen-crm.org/current/P144i_gained_member_by"
