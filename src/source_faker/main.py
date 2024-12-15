import os.path
import time
import schedule
import pandas as pd

from os import path
from datetime import timedelta
from urllib.parse import urlparse
from faker import Faker

from source_faker.logging_mixin import LoggingMixin


class SourceFaker(LoggingMixin):
    FILE_FORMATS: set[str] = {"JSON", "PARQUET"}

    def __init__(
        self,
        output_path: str,
        file_name: str,
        file_format: str,
        batch_rows: int = 100,
        batch_frequency_seconds: int = 10,
        duration_seconds: int = 60
    ):
        self.data_output = output_path
        self.file_name= file_name
        self.file_format = file_format
        self.batch_rows = batch_rows
        self.batch_frequency_seconds = batch_frequency_seconds
        self.duration_seconds = duration_seconds

        self.fake = Faker(use_weighting=False)
        self.file_index = 1

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

    def _validate(self):
        if self.file_format not in self.FILE_FORMATS:
            raise ValueError(f"Invalid file format {self.file_format}, allowed values {','.join(self.FILE_FORMATS)}")

        url = urlparse(self.data_output)
        if not url.scheme and not os.path.exists(self.data_output):
            os.makedirs(self.data_output)

    def _create_file(self):
        df = self._create_rows(self.batch_rows)
        full_path = path.join(self.data_output, f"{self.file_name}_{self.file_index:06d}.parquet")
        df.to_parquet(full_path)
        self.log.info(f"Created file {full_path}")
        self.file_index += 1

    def _create_rows(self, row_amount: int) -> pd.DataFrame:
        rows = []
        for i in range(1, row_amount+1):
            rows.append({
                "name": self.fake.name(),
                "address": self.fake.address(),
                "comment": self.fake.text()
            })
        return pd.DataFrame(rows)
