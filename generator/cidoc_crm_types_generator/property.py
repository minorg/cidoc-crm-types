from typing import NamedTuple

from rdflib import URIRef


class Property(NamedTuple):
    uri: URIRef
