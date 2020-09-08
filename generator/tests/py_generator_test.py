from pathlib import Path

from cidoc_crm_types_generator.ecrm_owl import EcrmOwl
from cidoc_crm_types_generator.py_generator import PyGenerator


def test_generate(ecrm_owl: EcrmOwl, tmpdir):
    PyGenerator(output_dir_path=Path(tmpdir)).generate(ecrm_owl=ecrm_owl)
    import sys
    sys.path.append(str(tmpdir))
    import cidoc_crm_types
    currency = cidoc_crm_types.E98Currency()
    assert currency._typename == "E98Currency"
