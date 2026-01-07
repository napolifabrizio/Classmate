from sqlalchemy import Column, TEXT, FLOAT, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.schema import Table, MetaData

TABLE_EXAMPLE = Table(
    "Example",
    MetaData(),
    Column("user_id", TEXT, primary_key=True),
    Column("created_at", TIMESTAMP),
    Column("areas", JSONB),
)
