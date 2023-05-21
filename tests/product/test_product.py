from inventory_report.inventory.product import Product
from faker import Faker
import random


def test_cria_produto():
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

    assert new_product.id == test_id
    assert new_product.nome_do_produto == test_name
    assert new_product.nome_da_empresa == test_corporation
    assert new_product.data_de_fabricacao == str(test_factory_date)
    assert new_product.numero_de_serie == test_serial_number
    assert new_product.instrucoes_de_armazenamento == test_storage_instructions
    assert new_product.data_de_validade == str(test_warranty_date)
