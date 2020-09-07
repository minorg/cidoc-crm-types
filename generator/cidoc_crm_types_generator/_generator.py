from abc import ABC, abstractmethod
from pathlib import Path


class _Generator(ABC):
    def __init__(self, *, root_dir_path: Path):
        self._root_dir_path = root_dir_path

    @abstractmethod
    def generate(self) -> None:
        """
        Generate files in the appropriate generic-specific directory.
        """
