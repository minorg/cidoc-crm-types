from .e28_conceptual_object import E28ConceptualObject
from .e72_legal_object import E72LegalObject
from dataclasses import dataclass


@dataclass
class E90SymbolicObject(E72LegalObject, E28ConceptualObject):
    """
Scope note:
This class comprises identifiable symbols and any aggregation of symbols, such as characters, identifiers, traffic signs, emblems, texts, data sets, images, musical scores, multimedia objects, computer program code or mathematical formulae that have an objectively recognizable structure and that are documented as single units.

It includes sets of signs of any nature, which may serve to designate something, or to communicate some propositional content. An instance of E90 Symbolic Object may or may not have a specific meaning, for example an arbitrary character string.

In some cases, the content of an instance of E90 Symbolic Object may completely be represented by a serialized digital content model, such as a sequence of ASCII-encoded characters, an XML or HTML document, or a TIFF image. The property P3 has note and its subproperty P190 has symbolic content allow for the description of this content model. In order to disambiguate which symbolic level is the carrier of the meaning, the property P3.1 has type can be used to specify the encoding (e.g. "bit", "Latin character", RGB pixel).


Examples:
- &#8216;ecognizabl&#8217;
- The &#8220;no-smoking&#8221; sign (E36)
- &#8220;BM000038850.JPG&#8221; (E41)
- image BM000038850.JPG from the Clayton Herbarium in London (E36)
- The distribution of form, tone and colour found on Leonardo da Vinci&#8217;s painting named &#8220;Mona Lisa&#8221; in daylight (E36)
- The Italian text of Dante&#8217;s &#8220;Divina Commedia&#8221; as found in the authoritative critical edition La Commedia secondo l&#8217;antica vulgata a cura di Giorgio Petrocchi, Milano: Mondadori, 1966-67 (= Le Opere di Dante Alighieri, Edizione Nazionale a cura della Societ&#224; Dantesca Italiana, VII, 1-4) (E33)


In First Order Logic:
E90(x) &#8835; E28(x)
E90(x) &#8835; E72(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E90_Symbolic_Object"
