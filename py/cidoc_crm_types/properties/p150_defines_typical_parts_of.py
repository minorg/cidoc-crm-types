from dataclasses import dataclass


@dataclass
class P150DefinesTypicalPartsOf:
    """
Scope note: 
This property associates an instance of E55 Type &#8220;A&#8221; with an instance of E55 Type &#8220;B&#8221;, when items of type &#8220;A&#8221; typically form part of items of type &#8220;B&#8221;, such as &#8220;car motors&#8221; and &#8220;cars&#8221;. The property is in general not transitive.

It allows types to be organised into hierarchies based on one type describing a typical part of another. This property is equivalent to "broader term partitive (BTP)" as defined in ISO 2788 and
&#8220;broaderPartitive&#8221; in SKOS.


Examples:
- Car motors (E55) defines typical parts of cars (E55)


In First Order Logic:
P150(x,y) &#8835; (E55 Type)
P150(x,y) &#8835; E55(y)
    """

    URI = "http://erlangen-crm.org/current/P150_defines_typical_parts_of"
