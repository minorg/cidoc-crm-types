from .p1i_identifies import P1iIdentifies
from dataclasses import dataclass


@dataclass
class P48iIsPreferredIdentifierOf(P1iIdentifies):
    URI = "http://erlangen-crm.org/current/P48i_is_preferred_identifier_of"
