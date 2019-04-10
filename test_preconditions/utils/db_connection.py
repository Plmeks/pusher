import os
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager


BD1_SETTINGS = dict(
    dbname="da",
    user="da",
    host=f"bd1.{os.environ['CLUSTER_TEST']}.notkube.dev.ivi.ru",
    port=5432,
)

AUTH_SETTINGS = dict(
    dbname="auth",
    user="auth",
    host=f"auth.{os.environ['CLUSTER_TEST']}.notkube.dev.ivi.ru",
    port=5432,
)

PROFIT_SETTINGS = dict(
    dbname="profit",
    user="da",
    host=f"profit.{os.environ['CLUSTER_TEST']}.notkube.dev.ivi.ru",
    port=5432,
)


class Cursor:
    def __init__(self, settings):
        self.settings = settings

    @contextmanager
    def context(self, cursor_factory=None):
        with psycopg2.connect(**self.settings) as conn:
            with conn.cursor(cursor_factory=cursor_factory) as cur:
                yield cur

    def execute(self, query):
        with self.context() as cur:
            cur.execute(query)

    def list_query(self, query):
        with self.context() as cur:
            cur.execute(query)
            result = [row[0] for row in cur.fetchall()]

        return result

    def dict_query(self, query):
        with self.context(RealDictCursor) as cur:
            cur.execute(query)
            result = cur.fetchall()

        return result


bd1_cursor = Cursor(BD1_SETTINGS)
auth_cursor = Cursor(AUTH_SETTINGS)
profit_cursor = Cursor(PROFIT_SETTINGS)
