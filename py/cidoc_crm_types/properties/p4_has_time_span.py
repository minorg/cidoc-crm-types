from dataclasses import dataclass


@dataclass
class P4HasTimeSpan:
    """
Scope note:
This property associates an instance of E2 Temporal Entity with the instance of E52 Time-Span during which it was on-going. The associated instance of E52 Time-Span is understood as the real time-span during which the phenomena making up the temporal entity instance were active. More than one instance of E52 Temporal Entity may share a common instance of E52 Time-Span only if they come into being and end being due to an identical declarations or events.


Examples:
- the Yalta Conference (E7) has time-span Yalta Conference time-span (E52)


In First Order Logic:
P4(x,y) &#8835; E2(x)
P4(x,y) &#8835; E52(y)
    """

    URI = "http://erlangen-crm.org/current/P4_has_time-span"
