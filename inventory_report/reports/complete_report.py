from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        report = super().generate(list)
        report += '\nProdutos estocados por empresa:\n'
        corporations_products = Counter([
            data['nome_da_empresa'] for data in list
        ])

        for corp, prods in corporations_products.items():
            report += f'- {corp}: {prods}\n'

        return report
