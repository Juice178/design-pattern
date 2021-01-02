from abc import ABC, abstractmethod
from typing import IO


class Writer:
    def __init__(self, file: IO) -> None:
        self._file = file

    @abstractmethod
    def write(self, content: str) -> None:
        pass


class FileWriter(Writer):
    def __init__(self, filename: str) -> None:
        super().__init__(open(filename, "w"))

    def write(self, content: str) -> None:
        self._file.write(f"{content}")
     
    def close(self) -> None:
        self._file.close()

