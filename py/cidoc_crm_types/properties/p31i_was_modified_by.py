from .p12i_was_present_at import P12iWasPresentAt
from dataclasses import dataclass


@dataclass
class P31iWasModifiedBy(P12iWasPresentAt):
    URI = "http://erlangen-crm.org/current/P31i_was_modified_by"
