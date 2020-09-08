from .e73_information_object import E73InformationObject
from dataclasses import dataclass


@dataclass
class E31Document(E73InformationObject):
    """
Scope note:
This class comprises identifiable immaterial items that make propositions about reality.

These propositions may be expressed in text, graphics, images, audiograms, videograms or by other similar means. Documentation databases are regarded as a special case of E31 Document. This class should not be confused with the term "document" in Information Technology, which is compatible with E73 Information Object.


Examples:
- the Encyclopaedia Britannica (E32) (Kogan, 1958)
- The image content of the photo of the Allied Leaders at Yalta published by UPI, 1945 (E38)
- the Doomsday Book


In First Order Logic:
E31(x) ? E73(x)
    """


