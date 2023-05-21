from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(cls, src_file):
        raise NotImplementedError
