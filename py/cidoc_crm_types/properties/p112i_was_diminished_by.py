from .p31i_was_modified_by import P31iWasModifiedBy
from dataclasses import dataclass


@dataclass
class P112iWasDiminishedBy(P31iWasModifiedBy):
    URI = "http://erlangen-crm.org/current/P112i_was_diminished_by"
