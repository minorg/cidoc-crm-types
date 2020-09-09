from .p94i_was_created_by import P94iWasCreatedBy
from dataclasses import dataclass


@dataclass
class P135iWasCreatedBy(P94iWasCreatedBy):
    URI = "http://erlangen-crm.org/current/P135i_was_created_by"
