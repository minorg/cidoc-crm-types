from .p157_is_at_rest_relative_to import P157IsAtRestRelativeTo
from dataclasses import dataclass


@dataclass
class P59iIsLocatedOnOrWithin(P157IsAtRestRelativeTo):
    URI = "http://erlangen-crm.org/current/P59i_is_located_on_or_within"
