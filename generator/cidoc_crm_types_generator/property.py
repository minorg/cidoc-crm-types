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
    def identifier(self):
        label = self.label
        if label is not None:
            label = label.strip()
        if not label:
            assert str(self.uri).startswith(str(BASE))
            label = str(self.uri)[len(str(BASE)) :]
            assert label
        snake_case_label = label.replace(" ", "_").replace("-", "_")
        camel_case_label = stringcase.camelcase(snake_case_label)
        return camel_case_label[0].upper() + camel_case_label[1:]
