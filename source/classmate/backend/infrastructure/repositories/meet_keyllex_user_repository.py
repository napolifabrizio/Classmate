from classmate.backend.infrastructure.repositories.repository_config import PostgreConnection
from classmate.backend.infrastructure.aurora_tables import TABLE_MEET_KEYLLEX_USER

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert


class MeetKeyllexUserRepo(PostgreConnection):
    def __init__(self):
        self._table = TABLE_MEET_KEYLLEX_USER

    def select_areas_by_user_id(self, user_id: int):
        query = select(self._table).where(self._table.c.user_id == user_id)
        response = self.execute_async_select(query)
        return response
