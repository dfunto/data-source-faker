from dataclasses import dataclass, field
from typing import Callable, Literal


@dataclass
class DatabaseColumn:
    column_name: str
    column_type: any
    generate: Callable
    category: str


@dataclass
class TableSettings:
    table_name: str
    output_path: str
    table_format: Literal['parquet', 'csv', 'json', 'text']
    columns: list[DatabaseColumn] = field(default_factory=lambda: [])
    columns_amount: int = 10  # if columns are not set, generate columns based on this param
    batch_frequency_seconds: int = 10
    duration_seconds: int = 60
    batch_rows: int = 100
