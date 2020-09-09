from .p15i_influenced import P15iInfluenced
from dataclasses import dataclass


@dataclass
class P136iSupportedTypeCreation(P15iInfluenced):
    URI = "http://erlangen-crm.org/current/P136i_supported_type_creation"
