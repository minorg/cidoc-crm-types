from .e13_attribute_assignment import E13AttributeAssignment
from dataclasses import dataclass


@dataclass
class E17TypeAssignment(E13AttributeAssignment):
    """
Scope note:
This class comprises the actions of classifying items of whatever kind. Such items include objects, specimens, people, actions and concepts.

This class allows for the documentation of the context of classification acts in cases where the value of the classification depends on the personal opinion of the classifier, and the date that the classification was made. This class also encompasses the notion of "determination," i.e. the systematic and molecular identification of a specimen in biology.


Examples:
- the first classification of object GE34604 as Lament Cloth, October 2nd
- the determination of a cactus in Martin Doerr's garden as 'Cereus hildmannianus K.Schumann', July 2003

In First Order Logic:
E17(x) ? E13(x)
    """

    _typename: str = 'E17TypeAssignment'
