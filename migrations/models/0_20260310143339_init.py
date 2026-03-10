from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJzVlF9LwzAUxb/K6JOCitZNxbdtICq6wRQRRErW3nVhaVKTW/+g++7mppvpOjcm+KBv67"
    "knyTk/kr0HmUpAmL02aB6Pg9PGeyBZBvZHbbLTCFiee50EZEPhrMx7hgY1i9GqIyYMWCkB"
    "E2ueI1fSqrIQgkQVWyOXqZcKyZ8KiFClgGPQdvDwaGUuE3gFM//MJ9GIg0gWovKEznZ6hG"
    "+50y4knjkjnTaMYiWKTHpz/oZjJb/cXCKpKUjQDIG2R11QfEo36zlvVCb1ljJiZU0CI1YI"
    "rNTdkEGsJPGzaYwrmNIpu+FB87h5cnjUPLEWl+RLOZ6W9Xz3cqEj0LsNpm7OkJUOh9Fzew"
    "ZtKNISvO6Y6e/pVZbUENrgdYRzYOsYzgUP0V+cX6KYsddIgEyRLnjYaq1hdtcedM/bgy3r"
    "2qY2yl7m8o73ZqOwnBFYD5Kexg8gzuz/E+DB/v4GAK1rJUA3WwRoT0Qo3+AixMubfu97iJ"
    "UlNZAJj7Hx0RDcLD3qvwF0DT/qS6EzY55EFdvWdfu+TrR71e+4/spgqt0uboOOpUt/lqNJ"
    "5dmTMGTx5IXpJFqaqFCt8i6PsjCrK0yy1LGixtPpJ7p5BNA="
)
