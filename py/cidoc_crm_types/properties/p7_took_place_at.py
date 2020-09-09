from dataclasses import dataclass


@dataclass
class P7TookPlaceAt:
    """
Scope note:
This property describes the spatial location of an instance of E4 Period.

The related instance of E53 Place should be seen as a wider approximation of the geometric area within which the phenomena that characterise the period in question occurred, see below. P7 took place at (witnessed) does not convey any meaning other than spatial positioning (frequently on the surface of the earth). For example, the period &#8220;R&#233;volution fran&#231;aise&#8221; can be said to have taken place in &#8220;France in 1789&#8221;; the &#8220;Victorian&#8221; period may be said to have taken place in &#8220;Britain from 1837- 1901&#8221; and its colonies, as well as other parts of Europe and North America. An instance of E4 Period can take place at multiple non-contiguous, non-overlapping locations.

It is a shortcut of the more fully developed path from E4 Period through P161 has spatial projection, E53 Place, P89 falls within to E53 Place. E4 Period is a subclass of E92 Spacetime Volume. By the definition of P161 has spatial projection an instance of E4 Period takes place on all its spatial projections, that is, instances of E53 Place. Something happening at a given place can also be considered to happen at a larger place containing the first. For example, the assault on the Bastille July 14th 1789 took place in the area covered by Paris in 1789 but also in the area covered by France in 1789. 


Examples 
- the period &#8220;R&#233;volution fran&#231;aise&#8221; (E4) took place at the area covered by France in 1789 (E53)


In First Order Logic:
P7(x,y) &#8835; E4(x)
P7(x,y) &#8835; E53(y)
    """

    URI = "http://erlangen-crm.org/current/P7_took_place_at"
