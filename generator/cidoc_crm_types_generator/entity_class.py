from dataclasses import dataclass
from typing import Optional, Tuple

from rdflib import URIRef

from cidoc_crm_types_generator._model import _Model
from cidoc_crm_types_generator.ecrm_owl_namespace import BASE
from cidoc_crm_types_generator.property_restriction import PropertyRestriction


@dataclass(frozen=True)
class EntityClass(_Model):
    disjoint_with: Optional[URIRef]
    notation: Optional[str]
    property_restrictions: Tuple[PropertyRestriction, ...]
    sub_class_of: Tuple[URIRef, ...]

    @property
    def snake_case_identifier(self):
        return self._label.replace(" ", "_").replace("-", "_").lower()

    @property
    def upper_camel_case_identifier(self):
        return self._label.replace(" ", "").replace("_", "").replace("-", "")
