from .p14i_performed import P14iPerformed
from dataclasses import dataclass


@dataclass
class P23iSurrenderedTitleThrough(P14iPerformed):
    URI = "http://erlangen-crm.org/current/P23i_surrendered_title_through"
