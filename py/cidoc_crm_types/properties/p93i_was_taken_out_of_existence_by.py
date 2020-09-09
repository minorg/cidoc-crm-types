from .p12i_was_present_at import P12iWasPresentAt
from dataclasses import dataclass


@dataclass
class P93iWasTakenOutOfExistenceBy(P12iWasPresentAt):
    URI = "http://erlangen-crm.org/current/P93i_was_taken_out_of_existence_by"
