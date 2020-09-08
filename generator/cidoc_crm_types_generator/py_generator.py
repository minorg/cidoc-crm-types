import dataclasses
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

from rdflib import URIRef

from cidoc_crm_types_generator._generator import _Generator
from cidoc_crm_types_generator.ecrm_owl import EcrmOwl
from cidoc_crm_types_generator.entity_class import EntityClass
from cidoc_crm_types_generator.property import Property
from cidoc_crm_types_generator.property_type import PropertyType


class PyGenerator(_Generator):
    _ROOT_MODULE_NAME = "cidoc_crm_types"
    _ENTITIES_MODULE_NAME = "entities"

    def generate(self, *, ecrm_owl: EcrmOwl):
        self.__generate_entity_classes(
            entity_classes_by_uri=ecrm_owl.entity_classes_by_uri,
            properties_by_uri=ecrm_owl.properties_by_uri,
        )

        self._write_file(
            self.output_dir_path / self._ROOT_MODULE_NAME / "__init__.py",
            """\
from .entities import *
""",
        )

    def __generate_entity_classes(
        self,
        *,
        entity_classes_by_uri: Dict[URIRef, EntityClass],
        properties_by_uri: Dict[URIRef, Property],
    ):
        effective_properties = [property_.effective_property(properties_by_uri=properties_by_uri) for property_ in properties_by_uri.values()]

        init_imports = []
        for entity_class in entity_classes_by_uri.values():
            imports = {"from dataclasses import dataclass"}
            if entity_class.sub_class_of:
                parent_class_names = []
                if entity_class.upper_camel_case_identifier == "E98Currency":
                    # E98 currency has an odd inheritance tree, which causes problems for Python:
                    # Cannot create a consistent method resolution order (MRO) for bases E55Type, E58MeasurementUnit
                    limit_sub_class_of = [sub_class_of for sub_class_of in entity_class.sub_class_of if entity_classes_by_uri[sub_class_of].upper_camel_case_identifier == "E58MeasurementUnit"]
                else:
                    limit_sub_class_of = entity_class.sub_class_of

                for sub_class_of in limit_sub_class_of:
                    parent_entity_class = entity_classes_by_uri[sub_class_of]
                    parent_class_names.append(parent_entity_class.upper_camel_case_identifier)
                    imports.add(
                        f"from .{parent_entity_class.snake_case_identifier} import {parent_entity_class.upper_camel_case_identifier}"
                    )
                parent_class_names = f"({', '.join(parent_class_names)})"
            else:
                parent_class_names = ""

            # entity_class_properties = [property_ for property_ in effective_properties if property_.domain == entity_class.uri]

            fields = []
            for effective_property in effective_properties:
                if effective_property.domain != entity_class.uri:
                    # The domain can be a superclass of this entity class, but then the field for that property will be in the Python superclass.
                    continue

                # Don't try to do range, get circular imports
                if effective_property.type == PropertyType.DATATYPE:
                    range_py_type = "object"
                    assert effective_property.range is None
                else:
                    range_py_type = entity_classes_by_uri[effective_property.range].upper_camel_case_identifier

                # Don't try to actually declare the range type, leads to circular imports
                fields.append(f"    {effective_property.snake_case_identifier}: Tuple[object, ...] = ()  # Range: {range_py_type}")
            if fields:
                imports.add("from typing import Tuple")
            fields = "\n".join(sorted(list(set(fields))))
            imports = "\n".join(sorted(list(set(imports))))

            if entity_class.comment:
                comment = f'''
    """
{entity_class.comment.encode("ascii", "replace").decode("ascii")}
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
{fields}
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
