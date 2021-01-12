class FileReader:
    def __init__(self, filename) -> None:
        self._file = open(filename, "r")

    def read_line(self) -> None:
        return self._file.readline()

    def close(self) -> None:
        self._file.close()

