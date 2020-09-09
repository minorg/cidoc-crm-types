from .e39_actor import E39Actor
from dataclasses import dataclass


@dataclass
class E74Group(E39Actor):
    """
Scope note:
This class comprises any gatherings or organizations of human individuals or groups that act collectively or in a similar way due to any form of unifying relationship. In the wider sense this class also comprises official positions which used to be regarded in certain contexts as one actor, independent of the current holder of the office, such as the president of a country. In such cases, it may happen that the group never had more than one member. A joint pseudonym (i.e., a name that seems indicative of an individual but that is actually used as a persona by two or more people) is a particular case of E74 Group.

A gathering of people becomes an instance of E74 Group when it exhibits organizational characteristics usually typified by a set of ideas or beliefs held in common, or actions performed together. These might be communication, creating some common artifact, a common purpose such as study, worship, business, sports, etc. Nationality can be modelled as membership in an instance of E74 Group (cf. HumanML markup). Married couples and other concepts of family are regarded as particular examples of E74 Group.


Examples:
- the impressionists (Wilson, 1983)
- the Navajo (Correll, 1972)
- the Greeks (Williams, 1993)
- the peace protestors in New York City on February 15 2003
- Exxon-Mobil (&#8216;Exxon Mobil Corp&#8217;, Mergent's dividend achievers, vol. 3, no. 3, 2006, pp. 97-97)
- King Solomon and his wives (Thieberger, 1947)
- The President of the Swiss Confederation
- Nicolas Bourbaki (Aczel, 2007)
- Betty Crocker (Crocker, 2012)
- Ellery Queen (Wheat, 2005)
- Greenpeace
- Paveprime Ltd
- the National Museum of Denmark


In First Order Logic:
E74(x) &#8835; E39(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E74_Group"
