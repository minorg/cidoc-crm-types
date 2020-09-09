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
&#61607; Minoan double axe mark 
&#61607; &#169;
&#61607; &#61514;


In First Order Logic:
E37(x) &#8835; E36(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E37_Mark"
