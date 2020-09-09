from dataclasses import dataclass
from typing import Optional

from rdflib import URIRef

from cidoc_crm_types_generator.ecrm_owl_namespace import BASE


@dataclass(frozen=True)
class _Model:
    comment: Optional[str]
    label: Optional[str]
    uri: URIRef

    @property
    def _uri_identifier(self):
        assert str(self.uri).startswith(str(BASE))
        return str(self.uri)[len(str(BASE)) :]
