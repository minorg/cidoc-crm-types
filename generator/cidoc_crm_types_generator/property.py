from dataclasses import dataclass
from typing import Optional, Tuple

import stringcase
from rdflib import URIRef

from cidoc_crm_types_generator._model import _Model
from cidoc_crm_types_generator.ecrm_owl_namespace import BASE
from cidoc_crm_types_generator.property_type import PropertyType


@dataclass(frozen=True)
class Property(_Model):
    domain: Optional[URIRef]
    inverse_of: Optional[URIRef]
    notation: Optional[str]
    range: Optional[URIRef]
    sub_property_of: Tuple[URIRef, ...]
    type: PropertyType

    @property
    def snake_case_identifier(self):
        return self._label.replace(" ", "_").replace("-", "_")

    @property
    def upper_camel_case_identifier(self):
        camel_case_identifier = stringcase.camelcase(self.snake_case_identifier)
        return camel_case_identifier[0].upper() + camel_case_identifier[1:]
