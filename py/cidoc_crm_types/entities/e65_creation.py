from dataclasses import dataclass
from .e7_activity import E7Activity
from .e63_beginning_of_existence import E63BeginningofExistence

@dataclass
class E65Creation(E7Activity, E63BeginningofExistence):
    pass
