from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, src_file):
        if src_file.endswith('.json'):
            with open(src_file) as file:
                data = json.load(file)
                return data
        raise ValueError('Arquivo inválido')
