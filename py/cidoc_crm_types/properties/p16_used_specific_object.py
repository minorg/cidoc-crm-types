from .p12_occurred_in_the_presence_of import P12OccurredInThePresenceOf
from .p15_was_influenced_by import P15WasInfluencedBy
from dataclasses import dataclass


@dataclass
class P16UsedSpecificObject(P12OccurredInThePresenceOf, P15WasInfluencedBy):
    """
Scope note:
This property describes the use of material or immaterial things in a way essential to the performance or the outcome of an instance of E7 Activity.

This property typically applies to tools, instruments, moulds, raw materials and items embedded in a product. It implies that the presence of the object in question was a necessary condition for the action. For example, the activity of writing this text required the use of a computer. An immaterial thing can be used if at least one of its carriers is present. For example, the software tools on a computer.

Another example is the use of a particular name by a particular group of people over some span to identify a thing, such as a settlement. In this case, the physical carriers of this name are at least the people understanding its use.


Examples:
- the writing of this scope note (E7) used specific object Nicholas Crofts' computer (E22) mode of use Typing Tool; Storage Medium (E55)
- the people of Iraq calling the place identified by TGN '7017998' (E7) used specific object "Quyunjig" (E44) mode of use Current; Vernacular (E55)


In First Order Logic:
P16 (x,y) &#8835; E7(x)
P16 (x,y) &#8835; E70(y)
P16 (x,y) &#8835; P12(x,y)
P16 (x,y) &#8835; P15(x,y)
P16(x,y,z) &#8835; [P16(x,y) &#8743; E55(z)]
    """

    URI = "http://erlangen-crm.org/current/P16_used_specific_object"
