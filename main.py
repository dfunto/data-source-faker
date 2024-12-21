from source_faker import SourceFaker
from source_faker.models import TableSettings, DatabaseColumn, ColumnType


def main():
    base_path = "./data"
    source_faker = SourceFaker(
        config_path=f"{base_path}/config.yaml"
    )
    source_faker.run()


if __name__ == "__main__":
    main()