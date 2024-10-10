from src.mock_data.ext import MockDataNotFound


class DataTypeEnum:
    CPF = "cpf"
    CNPJ = "cnpj"


class MockData:
    def __init__(self) -> None:
        pass

    def run(self, data_type: enumerate):
        try:
            getattr(DataTypeEnum, data_type)

        except AttributeError:
            raise MockDataNotFound(
                "Try choice one of that: 'cnpj', 'cpf', 'address'... see more running majinmock --help"
            )

    def generate_cnpj():
        print("generating cnpj")
