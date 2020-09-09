from dataclasses import dataclass


@dataclass
class P81OngoingThroughout:
    """
Scope note:
This property associates an instance of E52 Time-Span with an instance of E61 Time Primitive specifying a minimum period of time covered by it.

Since Time-Spans may not have precisely known temporal extents, there may be multiple minimum periods of . Union of

Examples:
- the time-span of the development of the CIDOC CRM (E52) ongoing throughout 1996-2002 (E61)

In First Order Logic:
P81 (x,y) &#8835; E52(x)
P81 (x,y) &#8835; E61(y)
    """

    URI = "http://erlangen-crm.org/current/P81_ongoing_throughout"
