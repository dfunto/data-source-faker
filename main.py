import time
import schedule
import pandas as pd

from datetime import timedelta
from pathlib import Path
from faker import Faker

class SourceFaker:
    def __init__(
        self,
        data_output: str = "./data",
        batch_rows: int = 100,
        batch_frequency_seconds: int = 10,
        duration_seconds: int = 60
    ):
        self.data_output = data_output
        self.batch_rows = batch_rows
        self.batch_frequency_seconds = batch_frequency_seconds
        self.duration_seconds = duration_seconds

        self.fake = Faker(use_weighting=False)
        self.file_index = 1

    def run(self):
        self._setup()

        (schedule
         .every(self.batch_frequency_seconds)
         .seconds
         .until(timedelta(seconds=self.duration_seconds))
         .do(self._create_files))

        while True:
            schedule.run_pending()
            time.sleep(1)
            if not schedule.next_run():
                return

    def _setup(self):
        Path(self.data_output).mkdir(parents=True, exist_ok=True)

    def _create_files(self):
        df = self._create_rows(self.batch_rows)
        df.to_parquet(f"{self.data_output}/sample_{self.file_index}.parquet")
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


def main():
    source_faker = SourceFaker()
    source_faker.run()


if __name__ == "__main__":
    main()