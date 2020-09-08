from .e63_beginning_of_existence import E63BeginningofExistence
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E67Birth(E63BeginningofExistence):
    """
Scope note:
This class comprises the births of human beings. E67 Birth is a biological event focussing on the context of people coming into life. (E63 Beginning of Existence comprises the coming into life of any living being).

Twins, triplets etc. are typically brought into life by the same instance of E67 Birth. The introduction of E67 Birth as a documentation element allows the description of a range of family relationships in a simple model. Suitable extensions may describe more details and the complexity of motherhood with the intervention of modern medicine. In this model, the biological father is not seen as a necessary participant in the birth.


Examples:
- the birth of Alexander the Great (Stoneman, 2004)


In First Order Logic:
E67(x) ? E63(x)
    """

    P97_from_father: Tuple[object, ...] = ()  # Range: E21Person
    __typename: str = 'E67Birth'
