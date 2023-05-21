from collections.abc import Iterable
from typing import Iterator
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, src_file, report_type):
        data = self.importer.import_data(src_file)
        self.data.extend(data)

        if report_type == 'simples':
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)

    def __iter__(self) -> Iterator:
        return InventoryIterator(self.data)
