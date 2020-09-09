from .p140i_was_attributed_by import P140iWasAttributedBy
from dataclasses import dataclass


@dataclass
class P39iWasMeasuredBy(P140iWasAttributedBy):
    URI = "http://erlangen-crm.org/current/P39i_was_measured_by"
