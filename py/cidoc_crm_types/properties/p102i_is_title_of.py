from .p1i_identifies import P1iIdentifies
from dataclasses import dataclass


@dataclass
class P102iIsTitleOf(P1iIdentifies):
    URI = "http://erlangen-crm.org/current/P102i_is_title_of"
