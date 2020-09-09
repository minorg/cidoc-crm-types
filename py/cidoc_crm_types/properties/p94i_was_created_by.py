from .p92i_was_brought_into_existence_by import P92iWasBroughtIntoExistenceBy
from dataclasses import dataclass


@dataclass
class P94iWasCreatedBy(P92iWasBroughtIntoExistenceBy):
    URI = "http://erlangen-crm.org/current/P94i_was_created_by"
