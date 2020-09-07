from dataclasses import dataclass
from .e90_symbolic_object import E90SymbolicObject
from .e89_propositional_object import E89PropositionalObject


@dataclass
class E73InformationObject(E90SymbolicObject, E89PropositionalObject):
    pass
