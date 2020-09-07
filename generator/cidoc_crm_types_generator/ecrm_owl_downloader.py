import logging
from pathlib import Path
from typing import Optional
from urllib.request import urlopen

from cidoc_crm_types_generator.path import ROOT_DIR_PATH


class EcrmOwlDownloader:
    def __init__(self):
        self.__logger = logging.getLogger(self.__class__.__name__)

    def download(
        self, *, from_url: Optional[str] = None, to_file_path: Optional[Path] = None
    ) -> Path:
        """
        Download the Erlangen CRM OWL file from the given URL to the given file path.

        If one or the other is not specified, a default will be used
        """

        if from_url is None:
            from_url = "https://raw.githubusercontent.com/erlangen-crm/ecrm/master/ecrm_current.owl"
        if to_file_path is None:
            to_file_path = ROOT_DIR_PATH / "generator" / "data" / "ecrm.owl"

        if to_file_path.is_file():
            self.__logger.info("%s already exists, skipping download", to_file_path)
            return to_file_path
        self.__logger.info("downloading %s to %s", from_url, to_file_path)
        try:
            f = urlopen(from_url)
            ecrm_owl = f.read()
        finally:
            f.close()
        with open(to_file_path, "w+b") as ecrm_owl_file:
            ecrm_owl_file.write(ecrm_owl)
        self.__logger.info("downloaded %s to %s", from_url, to_file_path)
        return to_file_path
