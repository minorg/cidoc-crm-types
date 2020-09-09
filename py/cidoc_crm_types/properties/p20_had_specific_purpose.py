from dataclasses import dataclass


@dataclass
class P20HadSpecificPurpose:
    """
Scope note:
This property identifies the relationship between a preparatory activity, an instance of E7 Activity and the instance of E7 Event it is intended to be preparation for.

This includes activities, orders and other organisational actions, taken in preparation for other activities or events.

P20 had specific purpose (was purpose of) implies that an activity succeeded in achieving its aim. If it does not succeed, such as the setting of a trap that did not catch anything, one may document the unrealized intention using P21 had general purpose (was purpose of): E55 Type and/or P33 used specific technique (was used by): E29 Design or Procedure.


Examples:
- Van Eyck's pigment grinding in 1432 (E7) had specific purpose the painting of the Ghent altar piece (E12)


In First Order Logic:
P21(x,y) &#8835; E7(x)
P21(x,y) &#8835; E55(y)
    """

    URI = "http://erlangen-crm.org/current/P20_had_specific_purpose"
