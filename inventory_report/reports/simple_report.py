import statistics
import datetime


class SimpleReport:
    @classmethod
    def generate(cls, list):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        older_factory_date = min([data['data_de_fabricacao'] for data in list])

        warranty_dates = [
            data['data_de_validade']
            for data in list
            if data['data_de_validade'] > today
        ]

        nearest_warranty_date = 'Nenhum'
        if len(warranty_dates) > 0:
            nearest_warranty_date = min(warranty_dates)

        corporation_with_more_products = statistics.mode([
            data['nome_da_empresa']
            for data in list
        ])

        return (
            f"Data de fabricação mais antiga: {older_factory_date}\n"
            f"Data de validade mais próxima: {nearest_warranty_date}\n"
            f"Empresa com mais produtos: {corporation_with_more_products}"
        )
