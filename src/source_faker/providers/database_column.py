from dataclasses import dataclass

from faker.providers import BaseProvider, ElementsType


@dataclass
class DatabaseColumn:
    column_name: str
    column_type: any
    category: str


class DatabaseColumnProvider(BaseProvider):

    database_columns: ElementsType[tuple[str, str, str]] =[
        ('id', 'SERIAL,BIGSERIAL,UUID', 'Identifiers'),
        ('uuid', 'UUID', 'Identifiers'),
        ('key', 'VARCHAR,TEXT', 'Identifiers'),
        ('slug', 'VARCHAR,TEXT', 'Identifiers'),
        ('username', 'VARCHAR,TEXT', 'User Information'),
        ('password', 'VARCHAR,TEXT', 'User Information'),
        ('email', 'VARCHAR,TEXT', 'User Information'),
        ('first_name', 'VARCHAR,TEXT', 'User Information'),
        ('last_name', 'VARCHAR,TEXT', 'User Information'),
        ('full_name', 'VARCHAR,TEXT', 'User Information'),
        ('display_name', 'VARCHAR,TEXT', 'User Information'),
        ('profile_pic', 'VARCHAR,TEXT', 'User Information'),
        ('avatar', 'VARCHAR,TEXT', 'User Information'),
        ('bio', 'TEXT', 'User Information'),
        ('created_at', 'TIMESTAMP', 'Timestamps'),
        ('updated_at', 'TIMESTAMP', 'Timestamps'),
        ('deleted_at', 'TIMESTAMP', 'Timestamps'),
        ('timestamp', 'TIMESTAMP', 'Timestamps'),
        ('last_modified', 'TIMESTAMP', 'Timestamps'),
        ('accessed_at', 'TIMESTAMP', 'Timestamps'),
        ('start_time', 'TIMESTAMP', 'Timestamps'),
        ('end_time', 'TIMESTAMP', 'Timestamps'),
        ('status', 'VARCHAR,TEXT', 'Status and Flags'),
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
        ('city', 'VARCHAR,TEXT', 'Geographical Data'),
        ('state', 'VARCHAR,TEXT', 'Geographical Data'),
        ('country', 'VARCHAR,TEXT', 'Geographical Data'),
        ('postal_code', 'VARCHAR,TEXT', 'Geographical Data'),
        ('zip_code', 'VARCHAR,TEXT', 'Geographical Data'),
        ('price', 'NUMERIC,FLOAT', 'Financial Data'),
        ('cost', 'NUMERIC,FLOAT', 'Financial Data'),
        ('amount', 'NUMERIC,FLOAT', 'Financial Data'),
        ('currency', 'VARCHAR,TEXT', 'Financial Data'),
        ('tax', 'NUMERIC,FLOAT', 'Financial Data'),
        ('discount', 'NUMERIC,FLOAT', 'Financial Data'),
        ('total_cost', 'NUMERIC,FLOAT', 'Financial Data'),
        ('balance', 'NUMERIC,FLOAT', 'Financial Data'),
        ('salary', 'NUMERIC,FLOAT', 'Financial Data'),
        ('payment_id', 'UUID', 'Financial Data'),
        ('date', 'DATE', 'Dates'),
        ('birth_date', 'DATE', 'Dates'),
        ('start_date', 'DATE', 'Dates'),
        ('end_date', 'DATE', 'Dates'),
        ('due_date', 'DATE', 'Dates'),
        ('expiration_date', 'DATE', 'Dates'),
        ('parent_id', 'UUID,INTEGER', 'Relationships'),
        ('child_id', 'UUID,INTEGER', 'Relationships'),
        ('user_id', 'UUID,INTEGER', 'Relationships'),
        ('customer_id', 'UUID,INTEGER', 'Relationships'),
        ('order_id', 'UUID,INTEGER', 'Relationships'),
        ('product_id', 'UUID,INTEGER', 'Relationships'),
        ('category_id', 'UUID,INTEGER', 'Relationships'),
        ('vendor_id', 'UUID,INTEGER', 'Relationships'),
        ('organization_id', 'UUID,INTEGER', 'Relationships'),
        ('team_id', 'UUID,INTEGER', 'Relationships'),
        ('title', 'VARCHAR,TEXT', 'Content and Text'),
        ('description', 'TEXT', 'Content and Text'),
        ('content', 'TEXT', 'Content and Text'),
        ('summary', 'TEXT', 'Content and Text'),
        ('details', 'TEXT', 'Content and Text'),
        ('notes', 'TEXT', 'Content and Text'),
        ('message', 'TEXT', 'Content and Text'),
        ('comments', 'TEXT', 'Content and Text')
     ]

    def database_column(self) -> DatabaseColumn:
        element = self.random_element(self.database_columns)
        return DatabaseColumn(
            column_name=element[0],
            column_type=element[1],
            category=element[2]
        )
