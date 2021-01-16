class Singleton:
    _singleton = None
    _has_created_before = False
    def __init__(self):
        if not self._has_created_before:
            # self.create_instance()
            cls._singleton = Singleton()
            self.update()
            print("An instance is created.")

    @classmethod
    def update(cls):
        cls._has_created_before = True

    @classmethod
    def create_instance(cls):
        cls._singleton = cls()
    
    @classmethod
    def get_instance(cls):
        return cls._singleton