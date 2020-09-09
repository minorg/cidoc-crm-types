from .p14i_performed import P14iPerformed
from dataclasses import dataclass


@dataclass
class P28iSurrenderedCustodyThrough(P14iPerformed):
    URI = "http://erlangen-crm.org/current/P28i_surrendered_custody_through"
