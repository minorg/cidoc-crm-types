from dataclasses import dataclass


@dataclass
class P139HasAlternativeForm:
    """
Scope note:
This property establishes a relationship of equivalence between two instances of E41 Appellation independent from any item identified by them. It is a dynamic asymmetric relationship, where the range expresses the derivative, if such a direction can be established. Otherwise, the relationship is symmetric.
The relationship is not transitive.

The equivalence applies to all cases of use of an instance of E41 Appellation. Multiple names assigned to an object, which are not equivalent for all things identified with a specific instance of E41 Appellation, should be modelled as repeated values of P1 is identified by (identifies).

P139.1 has type allows the type of derivation, such as &#8220;transliteration from Latin 1 to ASCII&#8221; be refined..


Examples:
- "Martin Doerr" (E41) has alternative form "Martin D&#246;rr" (E41) has type Alternate spelling (E55)
- "&#1043;&#1086;&#1085;&#1095;&#1072;&#1088;&#1086;&#1074;&#1072;, &#1053;&#1072;&#1090;&#1072;&#1083;&#1100;&#1103; &#1057;&#1077;&#1088;&#1075;&#1077;&#1077;&#1074;&#1085;&#1072;" (E41) has alternative form "Gon&#269;arova, Natal&#180;&#226; Sergeevna" (E41) has type ISO 9:1995 transliteration (E55)
- "&#913;&#952;&#942;&#957;&#945;" has alternative form "Athina" has type transcription.


In First Order Logic:
P139(x,y) &#8835; E41(x)
P139 (x,y) &#8835; E41(y)
P139(x,y,z) &#8835; [P139(x,y) &#8743; E55(z)]
P139(x,y) &#8835; P139(y,x)
    """

    URI = "http://erlangen-crm.org/current/P139_has_alternative_form"
