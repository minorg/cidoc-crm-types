from dataclasses import dataclass
from typing import Tuple


@dataclass
class E1CRMEntity:
    """
This class comprises all things in the universe of discourse of the CIDOC Conceptual Reference Model.

It is an abstract concept providing for three general properties:
1. Identification by name or appellation, and in particular by a preferred identifier
2. Classification by type, allowing further refinement of the specific subclass an instance belongs to
3. Attachment of free text and other unstructured data for the expression of anything not captured by formal properties

All other classes within the CIDOC CRM are directly or indirectly specialisations of E1 CRM Entity. 


Examples:
- the earthquake in Lisbon 1755 (E5) (Chester, 2001)


In First Order Logic: 
E1(x)
    """

    P100_died_in: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P100_was_death_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P102_is_title_of: Tuple[object, ...] = ()  # Range: E71ManMadeThing
    P108_has_produced: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P108_was_produced_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P109_has_current_or_former_curator: Tuple[object, ...] = ()  # Range: E39Actor
    P110_augmented: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P110_was_augmented_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P111_added: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P111_was_added_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P112_diminished: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P112_was_diminished_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P113_removed: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P113_was_removed_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P11_participated_in: Tuple[object, ...] = ()  # Range: E5Event
    P123_resulted_from: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P123_resulted_in: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P124_transformed: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P124_was_transformed_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P128_carries: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P128_is_carried_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P129_is_subject_of: Tuple[object, ...] = ()  # Range: E89PropositionalObject
    P134_continued: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P134_was_continued_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P135_created_type: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P135_was_created_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P136_supported_type_creation: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P136_was_based_on: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P137_exemplifies: Tuple[object, ...] = ()  # Range: E55Type
    P138_has_representation: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P138_represents: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P13_destroyed: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P13_was_destroyed_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P140_was_attributed_by: Tuple[object, ...] = ()  # Range: E13AttributeAssignment
    P141_was_assigned_by: Tuple[object, ...] = ()  # Range: E13AttributeAssignment
    P142_used_constituent: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P142_was_used_in: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P143_joined: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P143_was_joined_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P144_gained_member_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P144_joined_with: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P145_left_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P145_separated: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P146_lost_member_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P146_separated_from: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P14_carried_out_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P14_performed: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P151_participated_in: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P151_was_formed_from: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P15_influenced: Tuple[object, ...] = ()  # Range: E7Activity
    P164_is_restricted_by: Tuple[object, ...] = ()  # Range: E52TimeSpan
    P165_incorporates: Tuple[object, ...] = ()  # Range: E90SymbolicObject
    P166_was_a_presence_of: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P16_used_specific_object: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P16_was_used_for: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P17_motivated: Tuple[object, ...] = ()  # Range: E7Activity
    P180_has_currency: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P180i_was_currency_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P181_has_amount: Tuple[object, ...] = ()  # Range: object
    P1_is_identified_by: Tuple[object, ...] = ()  # Range: E41Appellation
    P22_acquired_title_through: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P22_transferred_title_to: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P23_surrendered_title_through: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P23_transferred_title_from: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P25_moved: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P25_moved_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P28_custody_surrendered_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P28_surrendered_custody_through: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P29_custody_received_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P29_received_custody_through: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P2_has_type: Tuple[object, ...] = ()  # Range: E55Type
    P31_has_modified: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P31_was_modified_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P33_used_specific_technique: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P33_was_used_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P34_concerned: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P35_has_identified: Tuple[object, ...] = ()  # Range: E3ConditionState
    P37_assigned: Tuple[object, ...] = ()  # Range: E42Identifier
    P38_deassigned: Tuple[object, ...] = ()  # Range: E42Identifier
    P39_measured: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P39_was_measured_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P3_has_note: Tuple[object, ...] = ()  # Range: object
    P40_observed_dimension: Tuple[object, ...] = ()  # Range: E54Dimension
    P41_classified: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P41_was_classified_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P42_assigned: Tuple[object, ...] = ()  # Range: E55Type
    P48_has_preferred_identifier: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P48_is_preferred_identifier_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P52_has_current_owner: Tuple[object, ...] = ()  # Range: E39Actor
    P55_has_current_location: Tuple[object, ...] = ()  # Range: E53Place
    P56_bears_feature: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P56_is_found_on: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P62_is_depicted_by: Tuple[object, ...] = ()  # Range: E24PhysicalManMadeThing
    P65_is_shown_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P65_shows_visual_item: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P67_is_referred_to_by: Tuple[object, ...] = ()  # Range: E89PropositionalObject
    P68_foresees_use_of: Tuple[object, ...] = ()  # Range: E57Material
    P70_documents: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P70_is_documented_in: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P71_is_listed_in: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P71_lists: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P73_has_translation: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P73_is_translation_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P92_brought_into_existence: Tuple[object, ...] = ()  # Range: E77PersistentItem
    P93_took_out_of_existence: Tuple[object, ...] = ()  # Range: E77PersistentItem
    P94_has_created: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P94_was_created_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P95_has_formed: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P95_was_formed_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P96_by_mother: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P96_gave_birth: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P98_brought_into_life: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P98_was_born: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P99_dissolved: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P99_was_dissolved_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P9_consists_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P9_forms_part_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
