from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, src_file):
        if src_file.endswith('.csv'):
            with open(src_file) as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                return data
        raise ValueError('Arquivo inválido')
