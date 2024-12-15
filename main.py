import argparse

from source_faker import SourceFaker

def setup_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_path", required=True ,help="Folder where the data will be output")
    parser.add_argument("--file_name", required=True, help="Name of the file, an index will be added for each file created (eg. sample_1.parquet, sample_2.parquet")
    parser.add_argument("--file_format", required=True, help=f"File format of the source: {','.join(SourceFaker.FILE_FORMATS)}", choices=SourceFaker.FILE_FORMATS, type=str.upper)
    parser.add_argument("--batch_frequency_seconds", type=int, help="Amount of seconds between each file creation")
    return parser.parse_args()


def main(args: argparse.Namespace):
    source_faker = SourceFaker(**vars(args))
    source_faker.run()


if __name__ == "__main__":
    parsed_args = setup_args()
    main(args=parsed_args)