from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def main():
    importers = {
        'csv': CsvImporter(),
        'json': JsonImporter(),
        'xml': XmlImporter(),
    }

    importer_type = ''
    if len(sys.argv) == 3:
        src_file = sys.argv[1]
        report_type = sys.argv[2]
        importer_type = sys.argv[1].split('.')[1]

    try:
        report = InventoryRefactor(
            importers[importer_type]
        ).import_data(src_file, report_type)

        sys.stdout.write(report)
    except KeyError:
        sys.stderr.write('Verifique os argumentos\n')


if __name__ == "__main__":
    main()
