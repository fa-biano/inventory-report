from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, src_file):
        if src_file.endswith('.xml'):
            with open(src_file) as file:
                reader = xmltodict.parse(file.read())
                data = [row for row in reader['dataset']['record']]
                return data
        raise ValueError('Arquivo inválido')
