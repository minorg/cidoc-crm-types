from dataclasses import dataclass


@dataclass
class P188RequiresProductionTool:
    """
Scope note: 
This property associates an instance of E99 Product Type with an instance of E19 Physical Object that is needed for the production of an instance of E18 Physical Thing. When the process of production is correctly executed in accordance with the plan and using the specified instance of E19 Physical Object, the resulting instance of E18 Physical Thing is considered an exemplar of this instance of E99 Product Type. The instance of E19 Physical Object may bear distinct features that are transformed into characteristic features of the resulting instance of E18 Physical Thing. Examples include models and moulds.


Examples:
- the luggage compartment lid mould (E19) for the Volkswagen Type 11 (Beetle) (E99) (https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Volkswagen_Type_1_(Auto_classique_St._Lazare_%2710).jpg/220pxVolkswagen_Type_1_(Auto_classique_St._Lazare_%2710).jpg)


In First Order Logic:
P188(x,y) &#8835; E99(x)
P188(x,y) &#8835; E19(y)
    """

    URI = "http://erlangen-crm.org/current/P188_requires_production_tool"
