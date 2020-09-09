from .p7i_witnessed import P7iWitnessed
from dataclasses import dataclass


@dataclass
class P26iWasDestinationOf(P7iWitnessed):
    URI = "http://erlangen-crm.org/current/P26i_was_destination_of"
