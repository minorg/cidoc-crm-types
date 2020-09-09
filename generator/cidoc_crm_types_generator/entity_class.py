from dataclasses import dataclass
from typing import Optional, Tuple

from rdflib import URIRef

from cidoc_crm_types_generator._model import _Model
from cidoc_crm_types_generator.property import Property
from cidoc_crm_types_generator.property_restriction import PropertyRestriction


@dataclass(frozen=True)
class EntityClass(_Model):
    disjoint_with: Optional[URIRef]
    notation: Optional[str]
    property_restrictions: Tuple[PropertyRestriction, ...]
    sub_class_of: Tuple[URIRef, ...]

    def is_sub_class_of(self, *, entity_classes_by_uri, parent_entity_class_uri: URIRef):
        if self.uri == parent_entity_class_uri:
            return True
        for sub_class_of in self.sub_class_of:
            if entity_classes_by_uri[sub_class_of].is_sub_class_of(parent_entity_class_uri=parent_entity_class_uri, entity_classes_by_uri=entity_classes_by_uri):
                return True
        return False

    @property
    def snake_case_identifier(self):
        return self._uri_identifier.replace(" ", "_").replace("-", "_").lower()

    @property
    def upper_camel_case_identifier(self):
        return self._uri_identifier.replace(" ", "").replace("_", "").replace("-", "")
