from .e11_modification import E11Modification
from .e63_beginning_of_existence import E63BeginningofExistence
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E12Production(E63BeginningofExistence, E11Modification):
    P186_produced_thing_of_product_type: Tuple[object, ...] = ()  # Range: E99ProductType
