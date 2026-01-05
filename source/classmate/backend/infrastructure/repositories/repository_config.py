from classmate.backend.infrastructure.environs import Environs

from sqlalchemy import create_engine
from sqlalchemy.engine import URL


class PostgreConnection:
    def __init__(self):
        self._environs = Environs()
        self._asyncSession = self.AsyncSession()

    def engine(self):
        url = URL.create(
            drivername="postgresql+psycopg2",
            username=self._environs.DB_USER,
            password=self._environs.DB_PASSWORD,
            host=self._environs.DB_HOST,
            port=self._environs.DB_PORT,
            database=self._environs.DB_NAME
        )
        engine = create_engine(
            url=url,
        )
        return engine

    def execute_select(self, query):
        with self._engine.connect() as conn:
            for row in conn.execute(query):
                return row

    def execute_commit(self, query):
        with self._engine.connect() as conn:
            conn.execute(query)
            conn.commit()
