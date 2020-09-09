from .p3_has_note import P3HasNote
from dataclasses import dataclass


@dataclass
class P79BeginningIsQualifiedBy(P3HasNote):
    """
Scope note:
This property associates an instance of E52 Time-Span with a note detailing the scholarly or scientific opinions and justifications about the certainty, precision, sources etc of its beginning. Such notes may also be used to elaborate arguments about constraints or to give explanations of alternatives.


Examples:
- the time-span of the Holocene (E52) beginning is qualified by &#8220;The formal definition and dating of the GSSP (GlobalStratotype Section and Point) for the base of theHolocene using the Greenland NGRIP ice core,and selected auxiliary records&#8221; (Walker et al 2009) (E62)


In First Order Logic:
P79 (x,y) &#8835; E52 (x)
P79 (x,y) &#8835; E62(y)
P79(x,y) &#8835; P3(x,y)
    """

    URI = "http://erlangen-crm.org/current/P79_beginning_is_qualified_by"
