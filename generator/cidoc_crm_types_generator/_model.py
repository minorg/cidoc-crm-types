from dataclasses import dataclass
from typing import Optional

from rdflib import URIRef


@dataclass(frozen=True)
class _Model:
    comment: Optional[str]
    label: Optional[str]
    uri: URIRef

    @property
    def identifier(self):
        label = self.label
        if label is None:
            uri_prefix = "http://erlangen-crm.org/current/"
            assert str(self.uri).startswith(uri_prefix)
            label = str(self.uri)[len(uri_prefix) :]
        return label.replace(" ", "").replace("_", "").replace("-", "")
