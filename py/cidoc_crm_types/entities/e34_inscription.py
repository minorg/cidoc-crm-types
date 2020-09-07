from dataclasses import dataclass
from .e33_linguistic_object import E33LinguisticObject
from .e37_mark import E37Mark

@dataclass
class E34Inscription(E33LinguisticObject, E37Mark):
    pass
