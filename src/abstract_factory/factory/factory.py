from factory.helper import Class
from abc import ABC, abstractmethod

class EmptyModule(Exception):
    pass

class Factory(ABC):
    @classmethod
    def get_factory(cls, class_name):
        try:
            factory = Class(class_name).new_instance()
        except Exception as e:
            raise Exception(e)
        return factory

    @abstractmethod
    def create_link(self, caption, url):
        pass

    @abstractmethod
    def create_tray(self, caption):
        pass

    @abstractmethod
    def create_page(self, title, author):
        pass

