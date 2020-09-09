from dataclasses import dataclass


@dataclass
class P1IsIdentifiedBy:
    """
Scope note:
This property describes the naming or identification of any real world item by a name or any other identifier.

This property is intended for identifiers in general use, which form part of the world the model intends to describe, and not merely for internal database identifiers which are specific to a technical system, unless these latter also have a more general use outside the technical context. This property includes in particular identification by mathematical expressions such as coordinate systems used for the identification of instances of E53 Place. The property does not reveal anything about when, where and by whom this identifier was used. A more detailed representation can be made using the fully developed (i.e. indirect) path through E15 Identifier Assignment.

P1 is identified by (identifies), is a shortcut for the path from &#8216;E1 CRM Entity&#8217; through &#8216;P140i was attributed by&#8217;, &#8216;E15 Identifier Assignment&#8217;, &#8216;P37 assigned&#8217;,&#8216;E42 Identifier&#8217;.


Examples:
- the capital of Italy (E53) is identified by "Rome" (E48)
- text 25014-32 (E33) is identified by "The Decline and Fall of the Roman Empire" (E35)


In First Order Logic:
P1(x,y) &#8835; E1(x)
P1(x,y) &#8835; E41(y)
    """

    URI = "http://erlangen-crm.org/current/P1_is_identified_by"
