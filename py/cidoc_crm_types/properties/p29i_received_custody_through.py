from .p14i_performed import P14iPerformed
from dataclasses import dataclass


@dataclass
class P29iReceivedCustodyThrough(P14iPerformed):
    URI = "http://erlangen-crm.org/current/P29i_received_custody_through"
