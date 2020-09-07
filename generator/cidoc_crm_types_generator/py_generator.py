from cidoc_crm_types_generator._generator import _Generator
from cidoc_crm_types_generator.ecrm_owl import EcrmOwl


class PyGenerator(_Generator):
    def generate(self, *, ecrm_owl: EcrmOwl):
        self._logger.info("writing output to %s", self._output_dir_path)

        # for entity_class in ecrm_owl.entity_classes_by_uri.values():
        #     print(entity_class.identifier)

        for property_ in ecrm_owl.properties_by_uri.values():
            print(property_.identifier)
