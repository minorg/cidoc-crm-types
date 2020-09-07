from dataclasses import dataclass
from .e41_appellation import E41Appellation
from .e33_linguistic_object import E33LinguisticObject


@dataclass
class E35Title(E41Appellation, E33LinguisticObject):
    pass
