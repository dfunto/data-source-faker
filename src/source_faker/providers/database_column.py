from collections.abc import Callable
from dataclasses import dataclass

from faker.providers import BaseProvider, ElementsType
from faker.providers.misc import Provider as MiscProvider
from faker.providers.lorem import Provider as LoremProvider
from faker.providers.date_time import Provider as DateProvider
from faker.providers.person import Provider as PersonProvider

@dataclass
class DatabaseColumn:
    column_name: str
    column_type: any
    generate: Callable
    category: str


class DatabaseColumnProvider(BaseProvider):

    database_columns: ElementsType[tuple[str, str, str]] = [
        ('id', 'SERIAL', 'Identifiers'),
        ('uuid', 'UUID', 'Identifiers'),
        ('key', 'VARCHAR', 'Identifiers'),
        ('slug', 'VARCHAR', 'Identifiers'),
        ('username', 'VARCHAR', 'User Information'),
        ('password', 'VARCHAR', 'User Information'),
        ('email', 'VARCHAR', 'User Information'),
        ('first_name', 'VARCHAR', 'User Information'),
        ('last_name', 'VARCHAR', 'User Information'),
        ('full_name', 'VARCHAR', 'User Information'),
        ('display_name', 'VARCHAR', 'User Information'),
        ('profile_pic', 'VARCHAR', 'User Information'),
        ('avatar', 'VARCHAR', 'User Information'),
        ('bio', 'TEXT', 'User Information'),
        ('created_at', 'TIMESTAMP', 'Timestamps'),
        ('updated_at', 'TIMESTAMP', 'Timestamps'),
        ('deleted_at', 'TIMESTAMP', 'Timestamps'),
        ('timestamp', 'TIMESTAMP', 'Timestamps'),
        ('last_modified', 'TIMESTAMP', 'Timestamps'),
        ('accessed_at', 'TIMESTAMP', 'Timestamps'),
        ('start_time', 'TIMESTAMP', 'Timestamps'),
        ('end_time', 'TIMESTAMP', 'Timestamps'),
        ('status', 'VARCHAR', 'Status and Flags'),
        ('is_active', 'BOOLEAN', 'Status and Flags'),
        ('is_deleted', 'BOOLEAN', 'Status and Flags'),
        ('is_verified', 'BOOLEAN', 'Status and Flags'),
        ('is_enabled', 'BOOLEAN', 'Status and Flags'),
        ('is_default', 'BOOLEAN', 'Status and Flags'),
        ('is_archived', 'BOOLEAN', 'Status and Flags'),
        ('count', 'INTEGER', 'Counts and Metrics'),
        ('total', 'INTEGER', 'Counts and Metrics'),
        ('quantity', 'INTEGER', 'Counts and Metrics'),
        ('value', 'FLOAT', 'Counts and Metrics'),
        ('rank', 'INTEGER', 'Counts and Metrics'),
        ('score', 'FLOAT', 'Counts and Metrics'),
        ('points', 'INTEGER', 'Counts and Metrics'),
        ('latitude', 'FLOAT', 'Geographical Data'),
        ('longitude', 'FLOAT', 'Geographical Data'),
        ('address', 'TEXT', 'Geographical Data'),
        ('city', 'VARCHAR', 'Geographical Data'),
        ('state', 'VARCHAR', 'Geographical Data'),
        ('country', 'VARCHAR', 'Geographical Data'),
        ('postal_code', 'VARCHAR', 'Geographical Data'),
        ('zip_code', 'VARCHAR', 'Geographical Data'),
        ('price', 'NUMERIC', 'Financial Data'),
        ('cost', 'NUMERIC', 'Financial Data'),
        ('amount', 'NUMERIC', 'Financial Data'),
        ('currency', 'VARCHAR', 'Financial Data'),
        ('tax', 'NUMERIC', 'Financial Data'),
        ('discount', 'NUMERIC', 'Financial Data'),
        ('total_cost', 'NUMERIC', 'Financial Data'),
        ('balance', 'NUMERIC', 'Financial Data'),
        ('salary', 'NUMERIC', 'Financial Data'),
        ('payment_id', 'UUID', 'Financial Data'),
        ('date', 'DATE', 'Dates'),
        ('birth_date', 'DATE', 'Dates'),
        ('start_date', 'DATE', 'Dates'),
        ('end_date', 'DATE', 'Dates'),
        ('due_date', 'DATE', 'Dates'),
        ('expiration_date', 'DATE', 'Dates'),
        ('parent_id', 'UUID', 'Relationships'),
        ('child_id', 'UUID', 'Relationships'),
        ('user_id', 'UUID', 'Relationships'),
        ('customer_id', 'UUID', 'Relationships'),
        ('order_id', 'UUID', 'Relationships'),
        ('product_id', 'UUID', 'Relationships'),
        ('category_id', 'UUID', 'Relationships'),
        ('vendor_id', 'UUID', 'Relationships'),
        ('organization_id', 'UUID', 'Relationships'),
        ('team_id', 'UUID', 'Relationships'),
        ('title', 'VARCHAR', 'Content and Text'),
        ('description', 'TEXT', 'Content and Text'),
        ('content', 'TEXT', 'Content and Text'),
        ('summary', 'TEXT', 'Content and Text'),
        ('details', 'TEXT', 'Content and Text'),
        ('notes', 'TEXT', 'Content and Text'),
        ('message', 'TEXT', 'Content and Text'),
        ('comments', 'TEXT', 'Content and Text')
     ]

    def _get_provider(self, column_type: str) -> Callable:
        misc = MiscProvider(self.generator)
        date = DateProvider(self.generator)
        lorem = LoremProvider(self.generator)
        person = PersonProvider(self.generator)

        return {
            'BOOLEAN': misc.boolean,
            'DATE': date.date,
            'FLOAT': misc.random_number,
            'INTEGER': misc.random_int,
            'NUMERIC':  misc.random_number,
            'SERIAL': misc.random_int,
            'BIGSERIAL': misc.random_int,
            'UUID': misc.random_int,
            'TEXT': lambda _: "", #lorem.text, TODO Fix this, maybe this is not the way to reference other providers
            'TIMESTAMP': date.unix_time,
            'VARCHAR': person.name
        }[column_type]

    def database_column(self) -> DatabaseColumn:
        element = self.random_element(self.database_columns)
        return DatabaseColumn(
            column_name=element[0],
            column_type=element[1],
            generate=self._get_provider(element[1]),
            category=element[2]
        )
