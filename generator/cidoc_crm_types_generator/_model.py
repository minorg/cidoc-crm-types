from dataclasses import dataclass
from typing import Optional

from rdflib import URIRef


@dataclass(frozen=True)
class _Model:
    comment: Optional[str]
    label: Optional[str]
    uri: URIRef
