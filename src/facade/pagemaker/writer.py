from abc import ABC, abstractmethod


class Writer:
    def __init__(self, filename: str) -> None:
        self._filename = filename

    @abstractmethod
    def write(self, content: str) -> None:
        pass


class FileWriter(Writer):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)

    def write(self, content: str) -> None:
        with open(self._filename, "a") as file:
            file.write(f"{content}")

