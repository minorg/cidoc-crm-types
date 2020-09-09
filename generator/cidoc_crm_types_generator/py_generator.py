from typing import Dict

from rdflib import URIRef

from cidoc_crm_types_generator._generator import _Generator
from cidoc_crm_types_generator.ecrm_owl import EcrmOwl
from cidoc_crm_types_generator.entity_class import EntityClass
from cidoc_crm_types_generator.property import Property


class PyGenerator(_Generator):
    _ROOT_MODULE_NAME = "cidoc_crm_types"
    _ENTITIES_MODULE_NAME = "entities"
    _PROPERTIES_MODULE_NAME = "properties"

    def generate(self, *, ecrm_owl: EcrmOwl):
        self.__generate_entity_classes(
            entity_classes_by_uri=ecrm_owl.entity_classes_by_uri,
            properties_by_uri=ecrm_owl.properties_by_uri,
        )
        self.__generate_properties(entity_classes_by_uri=ecrm_owl.entity_classes_by_uri, properties_by_uri=ecrm_owl.properties_by_uri)

        self._write_file(
            self.output_dir_path / self._ROOT_MODULE_NAME / "__init__.py",
            """\
from .entities import *
from .properties import *
""",
        )

    def __generate_entity_classes(
        self,
        *,
        entity_classes_by_uri: Dict[URIRef, EntityClass],
        properties_by_uri: Dict[URIRef, Property],
    ):
        init_imports = []
        for entity_class in entity_classes_by_uri.values():
            imports = {"from dataclasses import dataclass"}
            if entity_class.sub_class_of:
                if len(entity_class.sub_class_of) == 1:
                    parent_entity_class_uris = entity_class.sub_class_of
                else:
                    # Eliminate the case where a child property is declared a subClassOf its parent and grandparent
                    parent_entity_class_uris = []
                    for sub_class_of_i, sub_class_of in enumerate(entity_class.sub_class_of):
                        for other_sub_class_of_i, other_sub_class_of in enumerate(entity_class.sub_class_of):
                            if other_sub_class_of_i == sub_class_of_i:
                                continue
                            if entity_classes_by_uri[sub_class_of].is_sub_class_of(parent_entity_class_uri=other_sub_class_of, entity_classes_by_uri=entity_classes_by_uri):
                                self._logger.debug("entity class %s: parent %s is a child of other parent %s, skipping %s", entity_class.uri, sub_class_of, other_sub_class_of, other_sub_class_of)
                                continue
                            parent_entity_class_uris.append(sub_class_of)

                parent_class_names = []
                for sub_class_of in parent_entity_class_uris:
                    parent_entity_class = entity_classes_by_uri[sub_class_of]
                    parent_class_names.append(parent_entity_class.upper_camel_case_identifier)
                    imports.add(
                        f"from .{parent_entity_class.snake_case_identifier} import {parent_entity_class.upper_camel_case_identifier}"
                    )
                parent_class_names = f"({', '.join(parent_class_names)})"
            else:
                parent_class_names = ""

            imports = "\n".join(sorted(list(set(imports))))

            if entity_class.comment:
                comment = f'''
    """
{entity_class.comment.encode("ascii", "xmlcharrefreplace").decode("ascii")}
    """
'''
            else:
                comment = ''

            self._write_file(
                self.output_dir_path
                / self._ROOT_MODULE_NAME
                / self._ENTITIES_MODULE_NAME
                / (entity_class.snake_case_identifier + ".py"),
                f"""\
{imports}


@dataclass
class {entity_class.upper_camel_case_identifier}{parent_class_names}:{comment}
    TYPE_URI = "{entity_class.uri}"
""",
            )
            init_imports.append(
                f"from .{entity_class.snake_case_identifier} import {entity_class.upper_camel_case_identifier}"
            )

        self._write_file(
            self.output_dir_path
            / self._ROOT_MODULE_NAME
            / self._ENTITIES_MODULE_NAME
            / "__init__.py",
            "\n".join(init_imports),
        )

    def __generate_properties(
            self,
            *,
            entity_classes_by_uri: Dict[URIRef, EntityClass],
            properties_by_uri: Dict[URIRef, Property],
    ):
        init_imports = []
        for property_ in properties_by_uri.values():
            imports = {"from dataclasses import dataclass"}
            if property_.sub_property_of:
                if len(property_.sub_property_of) == 1:
                    parent_property_uris = property_.sub_property_of
                else:
                    # Eliminate the case where a child property is declared a subPropertyOf its parent and grandparent
                    parent_property_uris = []
                    for sub_property_of_i, sub_property_of in enumerate(property_.sub_property_of):
                        for other_sub_property_of_i, other_sub_property_of in enumerate(property_.sub_property_of):
                            if other_sub_property_of_i == sub_property_of_i:
                                continue
                            if properties_by_uri[sub_property_of].is_sub_property_of(parent_property_uri=other_sub_property_of, properties_by_uri=properties_by_uri):
                                self._logger.debug("property %s: parent %s is a child of other parent %s, skipping %s", property_.uri, sub_property_of, other_sub_property_of, other_sub_property_of)
                                continue
                            parent_property_uris.append(sub_property_of)

                parent_class_names = []
                for sub_property_of in parent_property_uris:
                    parent_property_ = properties_by_uri[sub_property_of]
                    parent_class_names.append(parent_property_.upper_camel_case_identifier)
                    imports.add(
                        f"from .{parent_property_.snake_case_identifier} import {parent_property_.upper_camel_case_identifier}"
                    )
                parent_class_names = f"({', '.join(parent_class_names)})"
            else:
                parent_class_names = ""

            imports = "\n".join(sorted(list(set(imports))))

            if property_.comment:
                comment = f'''
    """
{property_.comment.encode("ascii", "xmlcharrefreplace").decode("ascii")}
    """
'''
            else:
                comment = ''

            self._write_file(
                self.output_dir_path
                / self._ROOT_MODULE_NAME
                / self._PROPERTIES_MODULE_NAME
                / (property_.snake_case_identifier + ".py"),
                f"""\
{imports}


@dataclass
class {property_.upper_camel_case_identifier}{parent_class_names}:{comment}
    URI = "{property_.uri}"
""",
                )
            init_imports.append(
                f"from .{property_.snake_case_identifier} import {property_.upper_camel_case_identifier}"
            )

        self._write_file(
            self.output_dir_path
            / self._ROOT_MODULE_NAME
            / self._PROPERTIES_MODULE_NAME
            / "__init__.py",
            "\n".join(init_imports),
            )
