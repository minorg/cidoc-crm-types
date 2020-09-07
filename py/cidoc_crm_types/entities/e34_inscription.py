from dataclasses import dataclass
from .e37_mark import E37Mark
from .e33_linguistic_object import E33LinguisticObject


@dataclass
class E34Inscription(E37Mark, E33LinguisticObject):
    pass
