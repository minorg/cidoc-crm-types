from .p10i_contains import P10iContains
from dataclasses import dataclass


@dataclass
class P166iHadPresence(P10iContains):
    URI = "http://erlangen-crm.org/current/P166i_had_presence"
