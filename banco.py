from peewee import *
import os


class BancoConfig:

    @staticmethod
    def banco():
        db1 = SqliteDatabase('banco.db', pragmas=(
            ('journal_mode', 'wal'),  # WAL-mode.
            ('cache_size', -64 * 1000),  # 64MB cache.
            ('synchronous', 0)))  # Let the OS manage syncing.

        db2 = PostgresqlDatabase(
            'pfjbzmar',  # Required by Peewee.
            user='pfjbzmar',  # Will be passed directly to psycopg2.
            password="e3vvH5pZZH_rdqfIBj7NFrW4hnS7n31C",  # Ditto.
            host='tantor.db.elephantsql.com')  # Ditto.

        # os.environ.get('BD_RPGMESA')
        # lembrar que "e3vvH5pZZH_rdqfIBj7NFrW4hnS7n31C" tem que ser retirado
        return db2