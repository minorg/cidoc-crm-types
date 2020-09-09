from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass


@dataclass
class E54Dimension(E1CRMEntity):
    """
Scope note:
This class comprises quantifiable properties that can be measured by some calibrated means and can be approximated by values, i.e. points or regions in a mathematical or conceptual space, such as natural or real numbers, RGB values etc.

An instance of E54 Dimension represents the true quantity, independent from its numerical approximation, e.g. in inches or in cm. The properties of the class E54 Dimension allow for expressing the numerical approximation of the values of instances of E54 Dimension. If the true values belong to a non-discrete space, such as spatial distances, it is recommended to record them as approximations by intervals or regions of indeterminacy enclosing the assumed true values. For instance, a length of 5 cm may be recorded as 4.5-5.5 cm, according to the precision of the respective observation. Note, that interoperability of values described in different units depends critically on the representation as value regions.

Numerical approximations in archaic instances of E58 Measurement Unit used in historical records should be preserved. Equivalents corresponding to current knowledge should be recorded as additional instances of E54 Dimension as appropriate.


Examples:
- The 250 metric ton weight of the Luxor Obelisk
- The 5.17 m height of the statue of David by Michaelangelo
- The 530.2 carats of the Great Star of Africa diamond
- The AD1262-1312, 1303-1384 calibrated C14 date for the Shroud of Turin
- The 33 m diameter of the Stonehenge Sarcen Circle
- The 755.9 foot length of the sides of the Great Pyramid at Giza 
- Christies&#8217; hammer price for &#8220;Vase with Fifteen Sunflowers&#8221; (E97) has currency British Pounds (E98)
- The time span of the Battle of Issos 333 B.C.E. (E52) had duration Battle of Issos duration (E54)


In First Order Logic:
E54(x) &#8835; E1(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E54_Dimension"
