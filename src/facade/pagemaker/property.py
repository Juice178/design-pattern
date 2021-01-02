import configparser


class Property:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
    def load(self, filename: str) -> configparser.ConfigParser:
        return self.config.read(filename)
