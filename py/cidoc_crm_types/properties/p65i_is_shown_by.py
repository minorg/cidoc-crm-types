from .p128i_is_carried_by import P128iIsCarriedBy
from dataclasses import dataclass


@dataclass
class P65iIsShownBy(P128iIsCarriedBy):
    URI = "http://erlangen-crm.org/current/P65i_is_shown_by"
