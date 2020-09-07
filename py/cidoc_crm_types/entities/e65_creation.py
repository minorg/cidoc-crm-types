from dataclasses import dataclass
from .e63_beginning_of_existence import E63BeginningofExistence
from .e7_activity import E7Activity


@dataclass
class E65Creation(E63BeginningofExistence, E7Activity):
    pass
