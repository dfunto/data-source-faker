from source_faker import SourceFaker
from source_faker.models import TableSettings


def main():
    source_faker = SourceFaker(
        output_path="./data",
    )
    source_faker.add_tables([
        TableSettings(
            table_name="table_1",
            table_format="parquet"
        ),
        TableSettings(
            table_name="table_2",
            table_format="parquet"
        )
    ])
    source_faker.run()


if __name__ == "__main__":
    main()