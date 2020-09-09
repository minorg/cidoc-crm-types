from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass


@dataclass
class E52TimeSpan(E1CRMEntity):
    """
Scope note:
This class comprises abstract temporal extents, in the sense of Galilean physics, having a beginning, an end and a duration.

Instances of E52 Time-Span have no semantic connotations about phenomena happening within the temporal extent they represent. They do not convey any meaning other than a positioning on the &#8220;timeline&#8221; of chronology. The actual extent of an instance of E52 Time-Span can be approximated by properties of E52 Time-Span giving inner and outer bounds in the form of dates (instances of E61 Time Primitive). Comparing knowledge about time-spans is fundamental for chronological reasoning.

Some instances of E52 Time-Span may be defined as the actual, in principle observable, temporal extent of instances of E2 Temporal Entity via the property P4 has time-span (is time-span of): E52 Time-Span. They constitute phenomenal time-spans as defined in CRMgeo (Doerr and Hiebel 2013). Since our knowledge of history is imperfect and physical phenomena are fuzzy in nature, the extent of phenomenal time-spans can only be described in approximation. An extreme case of approximation, might, for example, define an instance of E52 Time-Span having unknown beginning, end and duration. It may, nevertheless, be associated with other descriptions by which we can infer knowledge about it, such as in relative chronologies.

Some instances of E52 may be defined precisely as representing a declaration of a temporal extent, as, for instance, done in a business contract. They constitute declarative time-spans as defined in CRMgeo (Doerr and Hiebel 2013) and can be described via the property E61 Time Primitive P170 defines time (time is defined by): E52 Time-Span.

When used as a common E52 Time-Span for two events, it will nevertheless describe them as being simultaneous, even if nothing else is known.


Examples:
- 1961
- from 12-17-1993 to 12-8-1996
- 14h30 - 16h22 4th July 1945
- 9.30 am 1.1.1999 to 2.00 pm 1.1.1999
- duration of the Ming Dynasty (Chan, 2011)


In First Order Logic:
E52(x) &#8835; E1(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E52_Time-Span"
