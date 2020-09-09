from dataclasses import dataclass


@dataclass
class P189Approximates:
    """
Scope note: 
This property associates an instance of E53 Place with another instance of E53 Place, which is defined in the same reference space, and which is used to approximate the former. The property does not necessarily state the quality or accuracy of this approximation, but rather indicates the use of the first instance of place to approximate the second.
In common documentation practice, find or encounter spots e.g. in archaeology, botany or zoology are often related to the closest village, river or other named place without detailing the relation, e.g. if it is located within the village or in a certain distance of the specified place. In this case the stated &#8220;phenomenal&#8221; place found in the documentation can be seen as approximation of the actual encounter spot without more specific knowledge.
In more recent documentation often point coordinate information is provided that originates from GPS measurements or georeferencing from a map. This point coordinate information does not state the actual place of the encounter spot but tries to approximate it with a &#8220;declarative&#8221; place. The accuracy depends on the methodology used when creating the coordinates. It may be dependent on technical limitations like GPS accuracy but also on the method where the GPS location is taken in relation to the measured feature. If the methodology is known a maximum deviation from the measured point can be calculated and the encounter spot or feature may be related to the resulting circle using an instance of P171 at some place within.


Examples:
&#61607; [40&#176;31'17.9"N 21&#176;15'48.3"E] approximates Kastoria, Greece, TGN ID: 7010880. (coordinates from https://sws.geonames.org/735927)
&#61607; [40&#176;31'00.1"N 21&#176;16'00.1"E] approximates Kastoria, Greece, TGN ID: 7010880. (coordinates from http://vocab.getty.edu/page/tgn/7010880)
&#61607; [40&#176;04'60.0"N 22&#176;21'00.0"E] approximates Mount Olympus National Park, Greece (coordinates from https://www.geonames.org/6941814)


In First Order Logic:
P189(x,y) &#8835; E53(x)
P189(x,y) &#8835; E53 (y)
P189 (x,y,z) &#8835; [P189 (x,y) &#8743; E55(z)]
    """

    URI = "http://erlangen-crm.org/current/P189_approximates"
