from .e73_information_object import E73InformationObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E33LinguisticObject(E73InformationObject):
    P72_has_language: Tuple[object, ...] = ()  # Range: E56Language
