from dataclasses import dataclass
from .e28_conceptual_object import E28ConceptualObject
from .e72_legal_object import E72LegalObject


@dataclass
class E90SymbolicObject(E28ConceptualObject, E72LegalObject):
    pass
