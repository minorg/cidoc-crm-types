from .p11i_participated_in import P11iParticipatedIn
from .p93i_was_taken_out_of_existence_by import P93iWasTakenOutOfExistenceBy
from dataclasses import dataclass


@dataclass
class P99iWasDissolvedBy(P93iWasTakenOutOfExistenceBy, P11iParticipatedIn):
    URI = "http://erlangen-crm.org/current/P99i_was_dissolved_by"
