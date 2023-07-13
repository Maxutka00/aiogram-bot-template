import asyncpg


class Repo:
    def __init__(self, db: asyncpg.Pool):
        self.db = db
