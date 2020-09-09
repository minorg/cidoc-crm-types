from dataclasses import dataclass


@dataclass
class P86FallsWithin:
    """
Scope note:
This property describes the inclusion relationship between two instances of E52 Time-Span.

This property supports the notion that a the temporal extent of an instance of E52 Time-Span falls within the temporal extent of another instance of E52 Time-Span. It addresses temporal containment only, and no contextual link between the two instances of E52 Time-Span is implied.
This property is transitive.


Examples:
- the time-span of the Apollo 11 moon mission (E52) falls within the time-span of the reign of Queen Elizabeth II (E52)


In First Order Logic:
P86(x,y) &#8835; E52(x)
P86(x,y) &#8835; E52(y)
    """

    URI = "http://erlangen-crm.org/current/P86_falls_within"
