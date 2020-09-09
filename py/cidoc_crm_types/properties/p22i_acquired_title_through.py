from .p14i_performed import P14iPerformed
from dataclasses import dataclass


@dataclass
class P22iAcquiredTitleThrough(P14iPerformed):
    URI = "http://erlangen-crm.org/current/P22i_acquired_title_through"
