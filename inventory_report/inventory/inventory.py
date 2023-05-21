from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, src_file, report_type):
        with open(src_file) as file:
            if src_file.endswith(".csv"):
                reader = csv.DictReader(file)
                data = [row for row in reader]
            elif src_file.endswith(".json"):
                data = json.load(file)
            else:
                reader = xmltodict.parse(file.read())
                data = [row for row in reader['dataset']['record']]

            if report_type == 'simples':
                return SimpleReport.generate(data)
            return CompleteReport.generate(data)
