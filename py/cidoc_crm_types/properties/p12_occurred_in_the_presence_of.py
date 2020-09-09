from dataclasses import dataclass


@dataclass
class P12OccurredInThePresenceOf:
    """
Scope note:
This property describes the active or passive presence of an E77 Persistent Item in an instance of E5 Event without implying any specific role.

It documents known events in which an instance of E77 Persistent Item was present during the course of its life or history. For example, an object may be the desk, now in a museum on which a treaty was signed. The instance of E53 Place and the instance of E52 Time-Span where and when these events happened provide us with constraints about the presence of the related instance E77 Persistent Item in the past. Instances of E90 Symbolic Object, in particular information objects, are physically present in events via at least one of the instances of E18 Physical Thing carrying them. Note, that the human mind can be such a carrier. A precondition for a transfer of information to a person or another new physical carrier is the presence of the respective information object and this person or physical thing in one event.


Examples:
- Deckchair 42 (E19) was present at The sinking of the Titanic (E5)


In First Order Logic:
P12(x,y) &#8835; E5(x)
P12(x,y) &#8835; E77(y)
    """

    URI = "http://erlangen-crm.org/current/P12_occurred_in_the_presence_of"
