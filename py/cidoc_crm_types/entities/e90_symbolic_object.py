from .e28_conceptual_object import E28ConceptualObject
from .e72_legal_object import E72LegalObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E90SymbolicObject(E72LegalObject, E28ConceptualObject):
    """
Scope note:
This class comprises identifiable symbols and any aggregation of symbols, such as characters, identifiers, traffic signs, emblems, texts, data sets, images, musical scores, multimedia objects, computer program code or mathematical formulae that have an objectively recognizable structure and that are documented as single units.

It includes sets of signs of any nature, which may serve to designate something, or to communicate some propositional content. An instance of E90 Symbolic Object may or may not have a specific meaning, for example an arbitrary character string.

In some cases, the content of an instance of E90 Symbolic Object may completely be represented by a serialized digital content model, such as a sequence of ASCII-encoded characters, an XML or HTML document, or a TIFF image. The property P3 has note and its subproperty P190 has symbolic content allow for the description of this content model. In order to disambiguate which symbolic level is the carrier of the meaning, the property P3.1 has type can be used to specify the encoding (e.g. "bit", "Latin character", RGB pixel).


Examples:
- ?ecognizabl?
- The ?no-smoking? sign (E36)
- ?BM000038850.JPG? (E41)
- image BM000038850.JPG from the Clayton Herbarium in London (E36)
- The distribution of form, tone and colour found on Leonardo da Vinci?s painting named ?Mona Lisa? in daylight (E36)
- The Italian text of Dante?s ?Divina Commedia? as found in the authoritative critical edition La Commedia secondo l?antica vulgata a cura di Giorgio Petrocchi, Milano: Mondadori, 1966-67 (= Le Opere di Dante Alighieri, Edizione Nazionale a cura della Societ? Dantesca Italiana, VII, 1-4) (E33)


In First Order Logic:
E90(x) ? E28(x)
E90(x) ? E72(x)
    """

    P106_forms_part_of: Tuple[object, ...] = ()  # Range: E90SymbolicObject
    P106_is_composed_of: Tuple[object, ...] = ()  # Range: E90SymbolicObject
    P165i_is_incorporated_in: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P190_has_symbolic_content: Tuple[object, ...] = ()  # Range: object
    __typename: str = 'E90SymbolicObject'
