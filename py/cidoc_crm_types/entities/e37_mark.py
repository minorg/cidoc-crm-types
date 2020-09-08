from .e36_visual_item import E36VisualItem
from dataclasses import dataclass


@dataclass
class E37Mark(E36VisualItem):
    """
Scope note:
This class comprises symbols, signs, signatures or texts applied to instances of E24 Physical HumanMade Thing by arbitrary techniques in order to indicate the creator, owner, dedications, purpose, etc.

Instances of E37 Mark do not represent the actual image of a mark, but the abstract ideal, as they use to
be codified in reference documents that are used in cultural documentation.


Examples:
? Minoan double axe mark 
? ?
? ?


In First Order Logic:
E37(x) ? E36(x)
    """

    __typename: str = 'E37Mark'
