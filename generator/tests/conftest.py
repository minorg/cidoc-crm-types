import pytest
from rdflib import Graph

from cidoc_crm_types_generator.ecrm_owl import EcrmOwl
from cidoc_crm_types_generator.ecrm_owl_downloader import EcrmOwlDownloader
from cidoc_crm_types_generator.ecrm_owl_parser import EcrmOwlParser


@pytest.fixture
def ecrm_owl() -> EcrmOwl:
    ecrm_owl_file_path = EcrmOwlDownloader().download()
    ecrm_owl_graph = Graph()
    ecrm_owl_graph.parse(source=str(ecrm_owl_file_path), format="xml")
    return EcrmOwlParser().parse(ecrm_owl_graph)
