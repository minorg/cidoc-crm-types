from .e72_legal_object import E72LegalObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E18PhysicalThing(E72LegalObject):
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
