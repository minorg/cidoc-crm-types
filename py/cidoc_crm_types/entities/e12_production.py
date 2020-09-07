from dataclasses import dataclass
from .e11_modification import E11Modification
from .e63_beginning_of_existence import E63BeginningofExistence

@dataclass
class E12Production(E11Modification, E63BeginningofExistence):
    pass
