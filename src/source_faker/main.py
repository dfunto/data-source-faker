import os.path
import time
import schedule
import pandas as pd

from os import path
from datetime import timedelta
from urllib.parse import urlparse
from functools import cached_property
from faker import Faker

from source_faker.logging_mixin import LoggingMixin
from source_faker.providers import DatabaseColumnProvider
from source_faker.providers.database_column import DatabaseColumn


class SourceFaker(LoggingMixin):
    FILE_FORMATS: set[str] = {"JSON", "PARQUET"}

    def __init__(
        self,
        output_path: str,
        file_name: str,
        file_format: str,
        batch_rows: int = 100,
        batch_cols: int = 10,
        batch_frequency_seconds: int = 10,
        duration_seconds: int = 60
    ):
        self.data_output = output_path
        self.file_name= file_name
        self.file_format = file_format
        self.batch_rows = batch_rows
        self.batch_cols = batch_cols
        self.batch_frequency_seconds = batch_frequency_seconds
        self.duration_seconds = duration_seconds

        self.fake: Faker = self._faker_init()
        self.columns = self._create_columns(col_amount=batch_cols)
        self.file_index: int = 1

    def run(self):
        self._validate()

        (schedule
         .every(self.batch_frequency_seconds)
         .seconds
         .until(timedelta(seconds=self.duration_seconds))
         .do(self._create_file))

        while True:
            schedule.run_pending()
            time.sleep(1)
            if not schedule.next_run():
                return

    @cached_property
    def available_fields(self) -> list[str]:
        return [method for method in dir(self.fake) if not method.startswith("_")]

    @staticmethod
    def _faker_init() -> Faker:
        fake = Faker(use_weighting=False)
        fake.add_provider(DatabaseColumnProvider)
        return fake

    def _validate(self):
        if self.file_format not in self.FILE_FORMATS:
            raise ValueError(f"Invalid file format {self.file_format}, allowed values {','.join(self.FILE_FORMATS)}")

        url = urlparse(self.data_output)
        if not url.scheme and not os.path.exists(self.data_output):
            os.makedirs(self.data_output)

    def _create_columns(self, col_amount: int) -> list[DatabaseColumn]:
        return [
            self.fake.database_column()
            for i in range(1, col_amount + 1)
        ]

    def _create_file(self):
        full_path = path.join(
            self.data_output,
            f"{self.file_name}_{self.file_index:06d}.parquet"
        )

        df = self._create_rows(row_amount=self.batch_rows)
        df.to_parquet(full_path)

        self.log.info(f"Created file {full_path}")
        self.file_index += 1

    def _create_rows(self, row_amount: int) -> pd.DataFrame:
        rows = []
        for i in range(1, row_amount+1):
            row = {
                column.column_name: self.fake.name() # TODO Fix each column value
                for column in self.columns
            }
            rows.append(row)
        return pd.DataFrame(rows)
