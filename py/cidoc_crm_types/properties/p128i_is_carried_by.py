from .p130i_features_are_also_found_on import P130iFeaturesAreAlsoFoundOn
from dataclasses import dataclass


@dataclass
class P128iIsCarriedBy(P130iFeaturesAreAlsoFoundOn):
    URI = "http://erlangen-crm.org/current/P128i_is_carried_by"
