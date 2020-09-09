from dataclasses import dataclass


@dataclass
class P8TookPlaceOnOrWithin:
    """
Scope note:
This property describes the location of an instance of E4 Period with respect to an instance of E19 Physical Object.
P8 took place on or within (witnessed) is a shortcut of the more fully developed path from &#8216;E4 Period&#8217; through &#8216;P7 took place at&#8217;, &#8216;E53 Place&#8217;, &#8216;P156i is occupied by&#8217;, to &#8216;E18 Physical Thing&#8217;.

It describes a period that can be located with respect to the space defined by an E19 Physical Object such as a ship or a building. The precise geographical location of the object during the period in question may be unknown or unimportant.
For example, the French and German armistice of 22 June 1940 was signed in the same railway carriage as the armistice of 11 November 1918.


Examples:
- the coronation of Queen Elisabeth II (E7) took place on or within Westminster Abbey (E19)


In First Order Logic:
P8(x,y) &#8835; E4(x)
P8(x,y) &#8835; E18(y)
    """

    URI = "http://erlangen-crm.org/current/P8_took_place_on_or_within"
