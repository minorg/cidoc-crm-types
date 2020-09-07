import dataclasses
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

from rdflib import URIRef

from cidoc_crm_types_generator._generator import _Generator
from cidoc_crm_types_generator.ecrm_owl import EcrmOwl
from cidoc_crm_types_generator.entity_class import EntityClass
from cidoc_crm_types_generator.property import Property


class PyGenerator(_Generator):
    _ROOT_MODULE_NAME = "cidoc_crm_types"
    _ENTITIES_MODULE_NAME = "entities"

    @dataclass(frozen=True)
    class __PyEntityClass(EntityClass):
        @property
        def class_name(self):
            return self.upper_camel_case_identifier

        @property
        def module_name(self):
            return self.snake_case_identifier

    @dataclass(frozen=True)
    class __PyProperty(Property):
        pass

    def generate(self, *, ecrm_owl: EcrmOwl):
        entity_classes_by_uri = {
            entity_class.uri: self.__PyEntityClass(**dataclasses.asdict(entity_class))
            for entity_class in ecrm_owl.entity_classes_by_uri.values()
        }
        properties_by_uri = {
            property_.uri: self.__PyProperty(**dataclasses.asdict(property_))
            for property_ in ecrm_owl.properties_by_uri.values()
        }

        self.__generate_entity_classes(
            entity_classes_by_uri=entity_classes_by_uri,
            properties_by_uri=properties_by_uri,
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
        entity_classes_by_uri: Dict[URIRef, __PyEntityClass],
        properties_by_uri: Dict[URIRef, __PyProperty],
    ):
        init_imports = []
        for entity_class in entity_classes_by_uri.values():
            imports = []
            if entity_class.sub_class_of:
                parent_class_names = []
                if entity_class.class_name == "E98Currency":
                    # E98 currency has an odd inheritance tree, which causes problems for Python:
                    # Cannot create a consistent method resolution order (MRO) for bases E55Type, E58MeasurementUnit
                    limit_sub_class_of = [sub_class_of for sub_class_of in entity_class.sub_class_of if entity_classes_by_uri[sub_class_of].class_name == "E58MeasurementUnit"]
                else:
                    limit_sub_class_of = entity_class.sub_class_of

                for sub_class_of in limit_sub_class_of:
                    parent_entity_class = entity_classes_by_uri[sub_class_of]
                    parent_class_names.append(parent_entity_class.class_name)
                    imports.append(
                        f"from .{parent_entity_class.module_name} import {parent_entity_class.class_name}"
                    )
                parent_class_names = f"({', '.join(parent_class_names)})"
            else:
                parent_class_names = ""
            imports = "\n".join(imports)

            self._write_file(
                self.output_dir_path
                / self._ROOT_MODULE_NAME
                / self._ENTITIES_MODULE_NAME
                / (entity_class.module_name + ".py"),
                f"""\
from dataclasses import dataclass
{imports}

@dataclass
class {entity_class.class_name}{parent_class_names}:
    pass
""",
            )
            init_imports.append(
                f"from .{entity_class.module_name} import {entity_class.class_name}"
            )

        self._write_file(
            self.output_dir_path
            / self._ROOT_MODULE_NAME
            / self._ENTITIES_MODULE_NAME
            / "__init__.py",
            "\n".join(init_imports),
        )
