from dataclasses import dataclass


@dataclass
class P187HasProductionPlan:
    """
Scope note: 
This property associates an instance of E99 Product Type with an instance of E29 Design or Procedure that completely determines the production of instances of E18 Physical Thing. The resulting instances of E18 Physical Thing are considered exemplars of this instance of E99 Product Type when the process specified is correctly executed. Note that the respective instance of E29 Design or Procedure may not necessarily be fixed in a written/graphical form, and may require the use of tools or models unique to the product type. The same instance of E99 Product Type may be associated with several variant plans. 


Examples:
- the production plans (E29) for Volkswagen Type 11 (Beetle) (E99)


In First Order Logic:
P187(x,y) &#8835; E99(x)
P187(x,y) &#8835; E29(y)
    """

    URI = "http://erlangen-crm.org/current/P187_has_production_plan"
