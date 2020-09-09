from .e73_information_object import E73InformationObject
from dataclasses import dataclass


@dataclass
class E33LinguisticObject(E73InformationObject):
    """
Scope note:
This class comprises identifiable expressions in natural language or languages.

Instances of E33 Linguistic Object can be expressed in many ways: e.g. as written texts, recorded speech or sign language. However, the CRM treats instances of E33 Linguistic Object independently from the medium or method by which they are expressed. Expressions in formal languages, such as computer code or mathematical formulae, are not treated as instances of E33 Linguistic Object by the CRM. These should be modelled as instances of E73 Information Object.

The text of an instance of E33 Linguistic Object can be documented in a note by P3 has note: E62 String


Examples:
- the text of the Ellesmere Chaucer manuscript (Hilmo, 2004)
- the lyrics of the song "Blue Suede Shoes" (Cooper, 2008)
- the text of the Jabberwocky by Lewis Carroll (Carroll, 1981)
- the text of "Doktoro Jekyll kaj Sinjoro Hyde" (an Esperanto translation of Dr Jekyll and Mr Hyde). (Stevenson, 1909)


In First Order Logic:
E33(x) &#8835; E73(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E33_Linguistic_Object"
