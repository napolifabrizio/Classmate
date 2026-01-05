from sqlalchemy import Column, TEXT, FLOAT, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.schema import Table, MetaData

TABLE_MEET_KEYLLEX_USER = Table(
    "MeetKeyllexUser",
    MetaData(),
    Column("user_id", TEXT, primary_key=True),
    Column("created_at", TIMESTAMP),
    Column("areas", JSONB),
)
