from .e63_beginning_of_existence import E63BeginningofExistence
from .e64_end_of_existence import E64EndofExistence
from dataclasses import dataclass


@dataclass
class E81Transformation(E64EndofExistence, E63BeginningofExistence):
    """
Scope note:
This class comprises the events that result in the simultaneous destruction of one or more than one instance of E18 Physical Thing and the creation of one or more than one instance of E18 Physical Thing that preserves recognizable substance and structure from the first one(s) but has fundamentally different nature or identity.

Although the old and the new instances of E18 Physical Thing are treated as discrete entities having separate, unique identities, they are causally connected through an instance of E81 Transformation. The creation of the new instances of E18 Physical Thing directly causes the destruction of the old instances of E18 Physical Thing using or preserving some relevant substance and structure. Instances of E81 Transformation are therefore distinct from re-classifications (documented as instances of E17 Type Assignment) or modifications (documented as instances of E11 Modification) of objects that do not fundamentally change their nature or identity. Characteristic cases of instances of E81 Transformation are reconstructions and repurposing of historical buildings or ruins, fires leaving buildings in ruins, taxidermy of specimens in natural history.


Examples:
- the death and mummification of Tut-Ankh-Amun (transformation of Tut-Ankh-Amun from a living person to a mummy) (E69,E81,E7)


In First Order Logic:
E81(x) ? E63(x)
E81(x) ? E64(x)
    """

    _typename: str = 'E81Transformation'
