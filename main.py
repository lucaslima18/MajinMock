import typer
from src.mock_data.mock_data import MockData


def main(name: str):
    print(name)
    MockData().run(data_type=name.upper())


if __name__ == "__main__":
    typer.run(main)
