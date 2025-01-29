from data_source_faker import DataSourceFaker


def main():
    DataSourceFaker(
        config_path="examples/config.yaml"
    ).run()


if __name__ == "__main__":
    main()