from .e55_type import E55Type
from dataclasses import dataclass


@dataclass
class E56Language(E55Type):
    """
Scope note:
This class is a specialization of E55 Type and comprises the natural languages in the sense of concepts.

This type is used categorically in the model without reference to instances of it, i.e. the Model does not foresee the description of instances of instances of E56 Language, e.g.: &#8220;instances of Mandarin Chinese&#8221;.

It is recommended that internationally or nationally agreed codes and terminology are used to denote instances of E56 Language, such as those defined in ISO 639-1:2002 and later versions. 


Examples:
- el [Greek] (Palmer, 1980)
- en [English] (Wilson, 1983)
- eo [Esperanto] (Nuessel, 2000)
- es [Spanish] (Pineda, 1993)
- fr [French] (Rickard, 1974)


In First Order Logic:
E56(x) &#8835; E55(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E56_Language"
