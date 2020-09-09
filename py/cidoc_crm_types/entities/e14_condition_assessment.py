from .e13_attribute_assignment import E13AttributeAssignment
from dataclasses import dataclass


@dataclass
class E14ConditionAssessment(E13AttributeAssignment):
    """
Scope note:
This class describes the act of assessing the state of preservation of an object during a particular period.

The condition assessment may be carried out by inspection, measurement or through historical research. This class is used to document circumstances of the respective assessment that may be relevant to interpret its quality at a later stage, or to continue research on related documents.


Examples:
- last year's inspection of humidity damage to the frescos in the St. George chapel in our village


In First Order Logic:
E14(x) &#8835; E13(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E14_Condition_Assessment"
