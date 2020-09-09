from dataclasses import dataclass


@dataclass
class P82AtSomeTimeWithin:
    """
Scope note:
This property describes the maximum period of time within which an E52 Time-Span falls.

Since Time-Spans may not have precisely known temporal extents, the CIDOC CRM supports statements about the minimum and maximum temporal extents of Time-Spans. This property allows a Time-Span&#8217;s maximum temporal extent (i.e. its outer boundary) to be assigned an E61 Time Primitive value. Time Primitives are treated by the CIDOC CRM as application or system specific date intervals, and are not further analysed.


Examples:
- the time-span of the development of the CIDOC CRM (E52) at some time within 1992-infinity (E61)


In First Order Logic:
P82 (x,y) &#8835; E52(x)
P82 (x,y) &#8835; E61(y)
    """

    URI = "http://erlangen-crm.org/current/P82_at_some_time_within"
