import configparser
from pathlib import Path


class Database:
    @staticmethod
    def get_propetries(dbname: str):
        filename = f"{dbname}.txt"
        prop = configparser.ConfigParser()
        try:
            with open(Path(filename).absolute()) as f:
                prop.read_file(f)
        except IOError:
            print(f"File - {filename} is not found")
        return prop