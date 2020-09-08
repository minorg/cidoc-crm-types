from .e33_linguistic_object import E33LinguisticObject
from .e41_appellation import E41Appellation
from dataclasses import dataclass


@dataclass
class E35Title(E41Appellation, E33LinguisticObject):

