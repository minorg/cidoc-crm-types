from .e26_physical_feature import E26PhysicalFeature
from dataclasses import dataclass


@dataclass
class E27Site(E26PhysicalFeature):
    """
Scope note:
This class comprises pieces of land or sea floor. 

In contrast to the purely geometric notion of E53 Place, this class describes constellations of matter on the surface of the Earth or other celestial body, which can be represented by photographs, paintings and maps. 

Instances of E27 Site are composed of relatively immobile material items and features in a particular configuration at a particular location.

Examples:
- the Amazon river basin
- Knossos
- the Apollo 11 landing site
- Heathrow Airport
- the submerged harbour of the Minoan settlement of Gournia, Crete

In First Order Logic:
E27(x)&#8835; E26(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E27_Site"
