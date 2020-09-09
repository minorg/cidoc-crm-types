from .p31i_was_modified_by import P31iWasModifiedBy
from dataclasses import dataclass


@dataclass
class P110iWasAugmentedBy(P31iWasModifiedBy):
    URI = "http://erlangen-crm.org/current/P110i_was_augmented_by"
