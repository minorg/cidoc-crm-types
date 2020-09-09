from .p3_has_note import P3HasNote
from dataclasses import dataclass


@dataclass
class P80EndIsQualifiedBy(P3HasNote):
    """
Scope note:
This property associates an instance of E52 Time-Span with a note detailing the scholarly or scientific opinions and justifications about the certainty, precision, sources etc of its end. Such notes may also be used to elaborate arguments about constraints or to give explanations of alternatives.

Examples:
- the time-span of the Holocene (E52) end is qualified by &#8220;still ongoing&#8221; (E62)

In First Order Logic:
P80(x,y) &#8835; E52(x)
P80(x,y) &#8835; E62(y)
P80(x,y) &#8835; P3(x,y)
    """

    URI = "http://erlangen-crm.org/current/P80_end_is_qualified_by"
