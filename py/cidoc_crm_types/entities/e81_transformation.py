from dataclasses import dataclass
from .e63_beginning_of_existence import E63BeginningofExistence
from .e64_end_of_existence import E64EndofExistence

@dataclass
class E81Transformation(E63BeginningofExistence, E64EndofExistence):
    pass
