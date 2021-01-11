from file_reader import FileReader
from string_buffer import StringBuffer


class BigChar:
    def __init__(self, charname: str) -> None:
        self._charname = charname
        self._fontdata = None

        try:
            reader = FileReader(f"big{charname}.txt")
            buf = StringBuffer()
            while (line := reader.read_line() != None):
                buf.append(line)
                buf.append("\n")
            reader.close()
            self._fontdata = buf.to_string()
        except IOError as e:
            self._fontdata = charname

    def print(self) -> None:
        print(self._fontdata)

    
