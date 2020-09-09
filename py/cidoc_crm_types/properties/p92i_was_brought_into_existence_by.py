from .p12i_was_present_at import P12iWasPresentAt
from dataclasses import dataclass


@dataclass
class P92iWasBroughtIntoExistenceBy(P12iWasPresentAt):
    URI = "http://erlangen-crm.org/current/P92i_was_brought_into_existence_by"
