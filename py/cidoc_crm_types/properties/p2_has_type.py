from dataclasses import dataclass


@dataclass
class P2HasType:
    """
Scope note:
This property allows sub typing of CIDOC CRM entities - a form of specialisation &#8211; through the use of a terminological hierarchy, or thesaurus.

The CIDOC CRM is intended to focus on the high-level entities and relationships needed to describe data structures. Consequently, it does not specialise entities any further than is required for this immediate purpose. However, entities in the isA hierarchy of the CIDOC CRM may by specialised into any number of sub entities, which can be defined in the E55 Type hierarchy. E41 Appellation, for example, may be specialised into &#8220;e-mail address&#8221;, &#8220;telephone number&#8221;, &#8220;post office box&#8221;, &#8220;URL&#8221; etc. none of which figures explicitly in the CIDOC CRM hierarchy. A comprehensive explanation about refining CIDOC CRM concepts by E55 Type is given in the section &#8220;About Types&#8221; in the section on &#8220;Specific Modelling Constructs&#8221; of this document.


Examples:
- "enquiries@cidoc-crm.org" (E51) has type e-mail address (E55)


In First Order Logic:
P2(x,y) &#8835; E1(x)
P2(x,y) &#8835; E55(y)
    """

    URI = "http://erlangen-crm.org/current/P2_has_type"
