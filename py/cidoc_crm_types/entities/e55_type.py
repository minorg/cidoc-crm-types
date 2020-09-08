from .e28_conceptual_object import E28ConceptualObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E55Type(E28ConceptualObject):
    """
Scope note:
This class comprises concepts denoted by terms from thesauri and controlled vocabularies used to characterize and classify instances of CIDOC CRM classes. Instances of E55 Type represent concepts in contrast to instances of E41 Appellation which are used to name instances of CIDOC CRM classes.

E55 Type is the CIDOC CRM?s interface to domain specific ontologies and thesauri. These can be represented in the CIDOC CRM as subclasses of E55 Type, forming hierarchies of terms, i.e. instances of E55 Type linked via P127 has broader term (has narrower term): E55Type. Such hierarchies may be extended with additional properties. 


Examples:
- weight, length, depth [types of E54]
- portrait, sketch, animation [types of E38]
- French, English, German [E56]
- excellent, good, poor [types of E3]
- Ford Model T, chop stick [types of E22]
- cave, doline, scratch [types of E26]
- poem, short story [types of E33]
- wedding, earthquake, skirmish [types of E5]


In First Order Logic:
E55(x) ? E28(x)
    """

    P101_was_use_of: Tuple[object, ...] = ()  # Range: E70Thing
    P103_was_intention_of: Tuple[object, ...] = ()  # Range: E71ManMadeThing
    P125_was_type_of_object_used_in: Tuple[object, ...] = ()  # Range: E7Activity
    P127_has_broader_term: Tuple[object, ...] = ()  # Range: E55Type
    P127_has_narrower_term: Tuple[object, ...] = ()  # Range: E55Type
    P137_is_exemplified_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P150_defines_typical_parts_of: Tuple[object, ...] = ()  # Range: E55Type
    P150_defines_typical_wholes_for: Tuple[object, ...] = ()  # Range: E55Type
    P21_was_purpose_of: Tuple[object, ...] = ()  # Range: E7Activity
    P2_is_type_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P32_was_technique_of: Tuple[object, ...] = ()  # Range: E7Activity
    P42_was_assigned_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    __typename: str = 'E55Type'
