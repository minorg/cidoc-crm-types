from .p7i_witnessed import P7iWitnessed
from dataclasses import dataclass


@dataclass
class P27iWasOriginOf(P7iWitnessed):
    URI = "http://erlangen-crm.org/current/P27i_was_origin_of"
