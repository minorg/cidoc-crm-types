from .e63_beginning_of_existence import E63BeginningofExistence
from .e64_end_of_existence import E64EndofExistence
from dataclasses import dataclass


@dataclass
class E81Transformation(E64EndofExistence, E63BeginningofExistence):

