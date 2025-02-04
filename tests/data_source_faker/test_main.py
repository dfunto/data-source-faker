from data_source_faker import DataSourceFaker
from data_source_faker.models import TableSettings


class TestSourceFaker:

    def test_initialize(self):
        DataSourceFaker()

    def test_run_once(self):
        faker = DataSourceFaker()
        faker.add_tables(
            TableSettings(
                table_name="single_file",
                table_format="csv",
                output_path="data/single_file",
                run_once=True
            )
        )
        faker.run()