from .e72_legal_object import E72LegalObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E18PhysicalThing(E72LegalObject):
    """
Scope note:
This class comprises all persistent physical items with a relatively stable form, human-made or natural.

Depending on the existence of natural boundaries of such things, the CIDOC CRM distinguishes the instances of E19 Physical Object from instances of E26 Physical Feature, such as holes, rivers, pieces of land etc. Most instances of E19 Physical Object can be moved (if not too heavy), whereas features are integral to the surrounding matter. An instance of E18 Physical Thing occupies not only a particular geometric space at any instant of its existence, but in the course of its existence it also forms a trajectory through spacetime, which occupies a real, that is phenomenal, volume in spacetime. We include in the occupied space the space filled by the matter of the physical thing and all its inner spaces, such as the interior of a box. For the purpose of more detailed descriptions of the presence of an instance of E18 Physical Thing in space and time it can be associated with its specific instance of E92 Spacetime Volume by the property P196 defines (is defined by).

The CIDOC CRM is generally not concerned with amounts of matter in fluid or gaseous states, as long as they are not confined in an identifiable way for an identifiable minimal time-span.


Examples:
- the Cullinan Diamond (E19) (Scarratt and Shor, 2006)
- the cave ?Ideon Andron? in Crete (E26) (Smith, 1844-49)
- the Mona Lisa (E22) (Mohem, 2006)


In First Order Logic:
E18(x) ? E72(x)
    """

    P156_occupies: Tuple[object, ...] = ()  # Range: E53Place
    P157_provides_reference_space_for: Tuple[object, ...] = ()  # Range: E53Place
    P195i_had_presence: Tuple[object, ...] = ()  # Range: E93SpacetimeSnapshot
    P196_defines: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P24_changed_ownership_through: Tuple[object, ...] = ()  # Range: E8Acquisition
    P30_custody_transferred_through: Tuple[object, ...] = ()  # Range: E10TransferofCustody
    P34_was_assessed_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P44_has_condition: Tuple[object, ...] = ()  # Range: E3ConditionState
    P45_consists_of: Tuple[object, ...] = ()  # Range: E57Material
    P46_forms_part_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P46_is_composed_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P49_has_former_or_current_keeper: Tuple[object, ...] = ()  # Range: E39Actor
    P50_has_current_keeper: Tuple[object, ...] = ()  # Range: E39Actor
    P51_has_former_or_current_owner: Tuple[object, ...] = ()  # Range: E39Actor
    P53_has_former_or_current_location: Tuple[object, ...] = ()  # Range: E53Place
    P59_has_section: Tuple[object, ...] = ()  # Range: E53Place
    P8_witnessed: Tuple[object, ...] = ()  # Range: E4Period
