from dataclasses import dataclass


@dataclass
class P54HasCurrentPermanentLocation:
    """
Scope note:
This property records the foreseen permanent location of an instance of E19 Physical Object at the time of validity of the record or database containing the statement that uses this property.

P54 has current permanent location (is current permanent location of) is similar to P55 has current location (currently holds). However, it indicates the E53 Place currently reserved for an object, such as the permanent storage location or a permanent exhibit location. The object may be temporarily removed from the permanent location, for example when used in temporary exhibitions or loaned to another institution. The object may never actually be located at its permanent location.


Examples:
- silver cup 232 (E22) has current permanent location Shelf 3.1, Store 2, Museum of Oxford (E53)

In First Order Logic:
P54(x,y) &#8835; E19(x)
P54(x,y) &#8835; E53(y)
    """

    URI = "http://erlangen-crm.org/current/P54_has_current_permanent_location"
