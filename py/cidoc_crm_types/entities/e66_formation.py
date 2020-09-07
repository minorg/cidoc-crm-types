from dataclasses import dataclass
from .e63_beginning_of_existence import E63BeginningofExistence
from .e7_activity import E7Activity


@dataclass
class E66Formation(E63BeginningofExistence, E7Activity):
    pass
