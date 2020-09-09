from .p31i_was_modified_by import P31iWasModifiedBy
from .p92i_was_brought_into_existence_by import P92iWasBroughtIntoExistenceBy
from dataclasses import dataclass


@dataclass
class P108iWasProducedBy(P92iWasBroughtIntoExistenceBy, P31iWasModifiedBy):
    URI = "http://erlangen-crm.org/current/P108i_was_produced_by"
