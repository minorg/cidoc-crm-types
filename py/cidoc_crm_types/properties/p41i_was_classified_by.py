from .p140i_was_attributed_by import P140iWasAttributedBy
from dataclasses import dataclass


@dataclass
class P41iWasClassifiedBy(P140iWasAttributedBy):
    URI = "http://erlangen-crm.org/current/P41i_was_classified_by"
