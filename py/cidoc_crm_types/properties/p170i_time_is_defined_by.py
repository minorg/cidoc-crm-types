from dataclasses import dataclass


@dataclass
class P170iTimeIsDefinedBy:
    """
Scope note:
This property associates an instance of E61 Time Primitive with the instance of E52 Time-Span that constitutes the interpretation of the terms of the time primitive as an extent in absolute, real time.


In First Order Logic:
P170(x,y) &#8835; E61(x)
P170(x,y) &#8835; E52(y)
    """

    URI = "http://erlangen-crm.org/current/P170i_time_is_defined_by"
