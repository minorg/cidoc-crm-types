from dataclasses import dataclass
from .e33_linguistic_object import E33LinguisticObject
from .e41_appellation import E41Appellation

@dataclass
class E35Title(E33LinguisticObject, E41Appellation):
    pass
