import asyncpg


class Repo:
    def __init__(self, conn: asyncpg.Pool):
        self.conn = conn
