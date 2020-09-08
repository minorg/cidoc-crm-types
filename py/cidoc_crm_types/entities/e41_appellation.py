from .e90_symbolic_object import E90SymbolicObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E41Appellation(E90SymbolicObject):
    """
Scope note:
This class comprises signs, either meaningful or not, or arrangements of signs following a specific syntax, that are used or can be used to refer to and identify a specific instance of some class or category within a certain context.

Instances of E41 Appellation do not identify things by their meaning, even if they happen to have one, but instead by convention, tradition, or agreement. Instances of E41 Appellation are cultural constructs; as such, they have a context, a history, and a use in time and space by some group of users. A given instance of E41 Appellation can have alternative forms, i.e., other instances of E41 Appellation that are always regarded as equivalent independent from the thing it denotes.

Different languages may use different appellations for the same thing, such as the names of major cities. Some appellations may be formulated using a valid noun phrase of a particular language. In these cases, the respective instances of E41 Appellation should also be declared as instances of E33 Linguistic Object. Then the language using the appellation can be declared with the property P72 has language: E56 Language.

Instances of E41 Appellation may be used to identify any instance of E1 CRM Entity and sometimes are characteristic for instances of more specific subclasses E1 CRM Entity, such as for instances of E52 Time-Span (for instance ?dates?), E39 Actor, E53 Place or E28 Conceptual Object. Postal addresses and E-mail addresses are characteristic examples of identifiers used by services transporting things between clients.

Even numerically expressed identifiers for extents in space or time are also regarded as instances of E41 Appellation, such as Gregorian dates or spatial coordinates, even though they allow for determining some time or location by a known procedure starting from a reference point and by virtue of that fact play a double role as instances of E59 Primitive Value.

E41 Appellation should not be confused with the act of naming something. Cf. E15 Identifier Assignment


Examples:
- "Martin" 
- ?Aquae Sulis Minerva?
- "the Merchant of Venice" (E35)
- "Spigelia marilandica (L.) L." [not the species, just the name] (Hershberger, Jenkins and Robacker, 2015)
- "information science" [not the science itself, but the name through which we refer to it in an English-speaking context] 
- ??? [Chinese "an", meaning "peace"]
- ?6?5?29?N 45?12?13?W? (example of spatial coordinate)
- ?Black queen?s bishop 4? [chess coordinate] (example of spatial coordinate)
- ?19-MAR-1922? (example of date)
- ?+41 22 418 5571? (example of contact point)
- "weasel@paveprime.com" (example of contact point)
- ?CH-1211, Gen?ve? (example of place appellation)
- ?1-29-3 Otsuka, Bunkyo-ku, Tokyo, 121, Japan? (example of address)
- ?the poop deck of H.M.S Victory? (example of section definition)
- ?the Venus de Milo?s left buttock? (example of section definition)


In First Order Logic:
E41(x) ? E90(x)
    """

    P139_has_alternative_form: Tuple[object, ...] = ()  # Range: E41Appellation
    P1_identifies: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P76_provides_access_to: Tuple[object, ...] = ()  # Range: E39Actor
