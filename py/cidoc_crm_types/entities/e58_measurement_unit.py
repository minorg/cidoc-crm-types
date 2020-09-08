from .e55_type import E55Type
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E58MeasurementUnit(E55Type):
    """
Scope note:
This class is a specialization of E55 Type and comprises the types of measurement units: feet, inches, centimetres, litres, lumens, etc.

This type is used categorically in the model without reference to instances of it, i.e. the Model does not foresee the description of instances of instances of E58 Measurement Unit, e.g.: ?instances of cm?.

Syst?me International (SI) units or internationally recognized non-SI terms should be used whenever possible, such as those defined by ISO80000:2009. Archaic Measurement Units used in historical records should be preserved.


Examples:
- cm [centimetre]
- km [kilometre]
- m [meter]
- m/s [meters per second] (Hau, 1999)
- A [Ampere]
- GRD [Greek Drachme] (Daniel, 2014) (E98)
- ?C [degrees centigrade] (Beckman, 1998)


In First Order Logic:
E58(x) ? E55(x)
    """

    P91_is_unit_of: Tuple[object, ...] = ()  # Range: E54Dimension
