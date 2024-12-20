import os.path
import time
from typing import Union, List

import schedule
import pandas as pd

from os import path
from datetime import timedelta
from urllib.parse import urlparse
from faker import Faker

from source_faker.logging_mixin import LoggingMixin
from source_faker.providers import DatabaseColumnProvider
from source_faker.models import DatabaseColumn, TableSettings


class SourceFaker(LoggingMixin):
    FILE_FORMATS: set[str] = {"json", "parquet"}

    def __init__(self):
        self.tables: list[TableSettings] = []
        self.fake: Faker = self._faker_init()

    def add_tables(self, tables: Union[TableSettings, List[TableSettings]]):
        if not isinstance(tables, list):
            tables = [tables]
        self.tables.extend(tables)

    def run(self):
        self._validate()

        for table in self.tables:
            if not table.columns:
                table.columns = self._create_columns(col_amount=table.columns_amount)

            (schedule
             .every(table.batch_frequency_seconds)
             .seconds
             .until(timedelta(seconds=table.duration_seconds))
             .do(self._create_file, table))

        while True:
            schedule.run_pending()
            time.sleep(1)
            if not schedule.next_run():
                return

    @staticmethod
    def _faker_init() -> Faker:
        fake = Faker(use_weighting=False)
        fake.add_provider(DatabaseColumnProvider)
        return fake

    def _validate(self):
        if not self.tables:
            raise ValueError(f"No tables defined, use the add_table method before running")

        # Create target directory if targeting the local file system
        for table in self.tables:
            url = urlparse(table.output_path)
            if not url.scheme and not os.path.exists(table.output_path):
                os.makedirs(table.output_path)

    def _create_columns(self, col_amount: int) -> list[DatabaseColumn]:
        return [self.fake.database_column() for _ in range(1, col_amount + 1)]

    def _create_file(self, table: TableSettings):
        current_timestamp = int(time.time())
        full_path = path.join(
            table.output_path,
            f"{table.table_name}_{current_timestamp}.parquet"
        )
        df = self._create_rows(table=table)
        df.to_parquet(full_path)

        self.log.info(f"Created file {full_path}")

    @staticmethod
    def _create_rows(table: TableSettings) -> pd.DataFrame:
        rows = []
        for i in range(1, table.batch_rows+1):
            row = {
                column.column_name: column.generate()
                for column in table.columns
            }
            rows.append(row)
        return pd.DataFrame(rows)
