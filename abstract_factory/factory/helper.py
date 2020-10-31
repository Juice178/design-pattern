class Class:
    def __init__(self, class_name):
        self._class_name = class_name
    def new_instance(self):
        parts = self._class_name.split('.')
        module = ".".join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp) 
        return m()