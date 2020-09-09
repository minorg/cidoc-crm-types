from .p140i_was_attributed_by import P140iWasAttributedBy
from dataclasses import dataclass


@dataclass
class P34iWasAssessedBy(P140iWasAttributedBy):
    URI = "http://erlangen-crm.org/current/P34i_was_assessed_by"
