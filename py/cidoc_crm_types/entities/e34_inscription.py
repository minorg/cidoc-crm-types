from .e33_linguistic_object import E33LinguisticObject
from .e37_mark import E37Mark
from dataclasses import dataclass


@dataclass
class E34Inscription(E37Mark, E33LinguisticObject):

