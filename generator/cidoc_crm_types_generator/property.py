import dataclasses
from dataclasses import dataclass
from typing import Optional, Tuple

import stringcase
from rdflib import URIRef

from cidoc_crm_types_generator._model import _Model
from cidoc_crm_types_generator.ecrm_owl_namespace import ROOT_ENTITY_CLASS_URI
from cidoc_crm_types_generator.property_type import PropertyType



@dataclass(frozen=True)
class Property(_Model):
    domain: Optional[URIRef]
    inverse_of: Optional[URIRef]
    notation: Optional[str]
    range: Optional[URIRef]
    sub_property_of: Tuple[URIRef, ...]
    type: PropertyType

    def effective_property(self, *, properties_by_uri):
        domains = []
        ranges = []

        # Traverse the hierarchy, appending to domain and ranges so that domains[0] is the closest domain value
        def visit_properties(property_uris: Tuple[URIRef, ...]):
            for property_uri in property_uris:
                property_ = properties_by_uri[property_uri]
                if property_.domain is not None:
                    domains.append(property_.domain)
                if property_.range is not None:
                    ranges.append(property_.range)
                visit_properties(property_.sub_property_of)
                if property_.inverse_of is not None:
                    inverse = properties_by_uri[property_.inverse_of]
                    # Don't recurse on the inverse
                    if inverse.domain is not None:
                        ranges.append(inverse.domain)
                    if inverse.range is not None:
                        domains.append(inverse.range)
        visit_properties((self.uri,))

        def dedupe_list(list_):
            unique = []
            for item in list_:
                if item not in unique:
                    unique.append(item)
            return unique

        domains = dedupe_list(domains)
        ranges = dedupe_list(ranges)

        if len(domains) == 0:
            domain = ROOT_ENTITY_CLASS_URI
        elif len(domains) == 1:
            domain = domains[0]
        elif len(domains) == 2:
            try:
                domains.remove(ROOT_ENTITY_CLASS_URI)
                domain = domains[0]
            except ValueError:
                domain = ROOT_ENTITY_CLASS_URI
        else:
            # Rather than doing the hard thing and calculating a type lattice, do the lazy thing and assume the root.
            domain = ROOT_ENTITY_CLASS_URI

        if len(ranges) == 0:
            assert self.type == PropertyType.DATATYPE, self.uri
            range = None
        elif len(ranges) == 1:
            range = ranges[0]
        elif len(ranges) == 2:
            try:
                ranges.remove(ROOT_ENTITY_CLASS_URI)
                range = ranges[0]
            except ValueError:
                range = ROOT_ENTITY_CLASS_URI
        else:
            range = ROOT_ENTITY_CLASS_URI

        # if len(domains) > 1 or len(ranges) > 1:
        #     print(self.uri, "domains and ranges:")
        #     print(" domains:", domains)
        #     print(" ranges:", ranges)
        #     print()

        # Take the most specific domain and range, which we assume was the first found in the bottom-up traversal
        kwds = dataclasses.asdict(self).copy()
        kwds["domain"] = domain
        kwds["range"] = range
        return self.__class__(**kwds)

    @property
    def snake_case_identifier(self):
        return self._label.replace(" ", "_").replace("-", "_")

    @property
    def upper_camel_case_identifier(self):
        camel_case_identifier = stringcase.camelcase(self.snake_case_identifier)
        return camel_case_identifier[0].upper() + camel_case_identifier[1:]
