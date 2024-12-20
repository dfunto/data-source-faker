from source_faker import SourceFaker
from source_faker.models import TableSettings


def main():
    base_path = "./data"
    source_faker = SourceFaker()
    source_faker.add_tables([
        TableSettings(
            table_name="table_3",
            table_format="parquet",
            output_path = f"{base_path}/table_3",
        )
    ])
    source_faker.run()


if __name__ == "__main__":
    main()