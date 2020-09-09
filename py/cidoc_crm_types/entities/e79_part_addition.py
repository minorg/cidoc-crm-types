from .e11_modification import E11Modification
from dataclasses import dataclass


@dataclass
class E79PartAddition(E11Modification):
    """
Scope note:
This class comprises activities that result in an instance of E24 Physical Human-Made Thing being increased, enlarged or augmented by the addition of a part.

Typical scenarios include the attachment of an accessory, the integration of a component, the addition of an element to an aggregate object, or the accessioning of an object into a curated instance of E78 Collection. Objects to which parts are added are, by definition, human-made, since the addition of a part implies a human activity. Following the addition of parts, the resulting human-made assemblages are treated objectively as single identifiable wholes, made up of constituent or component parts bound together either physically (for example the engine becoming a part of the car), or by sharing a common purpose (such as the 32 chess pieces that make up a chess set). This class of activities forms a basis for reasoning about the history and continuity of identity of objects that are integrated into other objects over time, such as precious gemstones being repeatedly incorporated into different items of jewellery, or cultural artifacts being added to different museum instances of E78 Collection over their lifespan.


Examples:
- the setting of the koh-i-noor diamond into the crown of Queen Elizabeth the Queen Mother (Dalrymple, 2017)
- the addition of the painting &#8220;Room in Brooklyn&#8221; by Edward Hopper to the collection of the Museum of Fine Arts, Boston


In First Order Logic:
E79(x) &#8835; E11(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E79_Part_Addition"
