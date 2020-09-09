from dataclasses import dataclass


@dataclass
class P191HadDuration:
    """
Scope note: 
This property describes the length of time covered by an instance of E52 Time-Span. It allows an instance of E52 Time-Span to be associated with an instance of E54 Dimension representing duration independent from the actual beginning and end. Indeterminacy of the duration value can be expressed by assigning a numerical interval to the property P90 has value of E54 Dimension.


Examples:
- the time span of the Battle of Issos 333 B.C.E. (E52) had duration Battle of Issos duration (E54)


In First Order Logic:
 P191(x,y) &#8835; E52(x)
 P191(x,y) &#8835; E54(y)
    """

    URI = "http://erlangen-crm.org/current/P191_had_duration"
