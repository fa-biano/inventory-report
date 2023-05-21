from inventory_report.inventory.product import Product
from faker import Faker
import random


def test_relatorio_produto():
    faker = Faker()

    test_id = random.randint(1, 20)
    test_name = faker.name()
    test_corporation = faker.name()
    test_factory_date = faker.date_of_birth()
    test_warranty_date = faker.date_between(
        test_factory_date,
        '+2y',
    )
    test_serial_number = pow(test_id, 3)
    test_storage_instructions = faker.name()

    new_product = Product(
        test_id,
        test_name,
        test_corporation,
        test_factory_date,
        test_warranty_date,
        test_serial_number,
        test_storage_instructions,
    )

    text_builder = [
        f'O produto {test_name}',
        f' fabricado em {test_factory_date}',
        f' por {test_corporation} com validade',
        f' até {test_warranty_date}',
        f' precisa ser armazenado {test_storage_instructions}.',
    ]

    expected_result = ''
    for text in text_builder:
        expected_result += text

    assert str(new_product) == expected_result
