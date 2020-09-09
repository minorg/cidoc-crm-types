from .e90_symbolic_object import E90SymbolicObject
from dataclasses import dataclass


@dataclass
class E41Appellation(E90SymbolicObject):
    """
Scope note:
This class comprises signs, either meaningful or not, or arrangements of signs following a specific syntax, that are used or can be used to refer to and identify a specific instance of some class or category within a certain context.

Instances of E41 Appellation do not identify things by their meaning, even if they happen to have one, but instead by convention, tradition, or agreement. Instances of E41 Appellation are cultural constructs; as such, they have a context, a history, and a use in time and space by some group of users. A given instance of E41 Appellation can have alternative forms, i.e., other instances of E41 Appellation that are always regarded as equivalent independent from the thing it denotes.

Different languages may use different appellations for the same thing, such as the names of major cities. Some appellations may be formulated using a valid noun phrase of a particular language. In these cases, the respective instances of E41 Appellation should also be declared as instances of E33 Linguistic Object. Then the language using the appellation can be declared with the property P72 has language: E56 Language.

Instances of E41 Appellation may be used to identify any instance of E1 CRM Entity and sometimes are characteristic for instances of more specific subclasses E1 CRM Entity, such as for instances of E52 Time-Span (for instance &#8220;dates&#8221;), E39 Actor, E53 Place or E28 Conceptual Object. Postal addresses and E-mail addresses are characteristic examples of identifiers used by services transporting things between clients.

Even numerically expressed identifiers for extents in space or time are also regarded as instances of E41 Appellation, such as Gregorian dates or spatial coordinates, even though they allow for determining some time or location by a known procedure starting from a reference point and by virtue of that fact play a double role as instances of E59 Primitive Value.

E41 Appellation should not be confused with the act of naming something. Cf. E15 Identifier Assignment


Examples:
- "Martin" 
- &#8220;Aquae Sulis Minerva&#8221;
- "the Merchant of Venice" (E35)
- "Spigelia marilandica (L.) L." [not the species, just the name] (Hershberger, Jenkins and Robacker, 2015)
- "information science" [not the science itself, but the name through which we refer to it in an English-speaking context] 
- &#8220;&#23433;&#8221; [Chinese "an", meaning "peace"]
- &#8220;6&#176;5&#8217;29&#8221;N 45&#176;12&#8217;13&#8221;W&#8221; (example of spatial coordinate)
- &#8220;Black queen&#8217;s bishop 4&#8221; [chess coordinate] (example of spatial coordinate)
- &#8220;19-MAR-1922&#8221; (example of date)
- &#8220;+41 22 418 5571&#8221; (example of contact point)
- "weasel@paveprime.com" (example of contact point)
- &#8220;CH-1211, Gen&#232;ve&#8221; (example of place appellation)
- &#8220;1-29-3 Otsuka, Bunkyo-ku, Tokyo, 121, Japan&#8221; (example of address)
- &#8220;the poop deck of H.M.S Victory&#8221; (example of section definition)
- &#8220;the Venus de Milo&#8217;s left buttock&#8221; (example of section definition)


In First Order Logic:
E41(x) &#8835; E90(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E41_Appellation"
