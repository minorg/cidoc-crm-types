import logging
from abc import ABC, abstractmethod
from pathlib import Path

from cidoc_crm_types_generator.ecrm_owl import EcrmOwl


class _Generator(ABC):
    def __init__(self, *, output_dir_path: Path):
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__output_dir_path = output_dir_path

    @abstractmethod
    def generate(self, *, ecrm_owl: EcrmOwl) -> None:
        """
        Generate files in the appropriate generic-specific directory.
        """

    @classmethod
    def language(cls) -> str:
        """
        Return the language of the generator, such as 'py'.
        """
        return cls.__name__.rstrip("Generator").lower()

    @property
    def _logger(self):
        return self.__logger

    @property
    def _output_dir_path(self):
        return self.__output_dir_path
