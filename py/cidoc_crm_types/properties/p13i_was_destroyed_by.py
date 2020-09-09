from .p93i_was_taken_out_of_existence_by import P93iWasTakenOutOfExistenceBy
from dataclasses import dataclass


@dataclass
class P13iWasDestroyedBy(P93iWasTakenOutOfExistenceBy):
    URI = "http://erlangen-crm.org/current/P13i_was_destroyed_by"
