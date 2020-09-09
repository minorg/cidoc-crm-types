from .p130_shows_features_of import P130ShowsFeaturesOf
from dataclasses import dataclass


@dataclass
class P73iIsTranslationOf(P130ShowsFeaturesOf):
    URI = "http://erlangen-crm.org/current/P73i_is_translation_of"
