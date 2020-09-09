from .p53i_is_former_or_current_location_of import P53iIsFormerOrCurrentLocationOf
from dataclasses import dataclass


@dataclass
class P55iCurrentlyHolds(P53iIsFormerOrCurrentLocationOf):
    URI = "http://erlangen-crm.org/current/P55i_currently_holds"
