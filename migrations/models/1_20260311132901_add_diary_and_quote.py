from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(100) NOT NULL UNIQUE,
    "password_hash" VARCHAR(255) NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_users_usernam_266d85" ON "users" ("username");
        CREATE TABLE IF NOT EXISTS "diaries" (
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(50) NOT NULL,
    "content" TEXT NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "quotes" (
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "id" SERIAL NOT NULL PRIMARY KEY,
    "content" TEXT NOT NULL,
    "author" VARCHAR(100) NOT NULL DEFAULT 'Anonymous'
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "users";
        DROP TABLE IF EXISTS "quotes";
        DROP TABLE IF EXISTS "diaries";"""


MODELS_STATE = (
    "eJztWV1vmzAU/SsRT620TW3WtNXeaJquWdtka9lWdZqQAw5YBZtiszTq+O+zDYSvwJKqtI"
    "nEGxzfi+891/Y9wJPiEhM69MN3Cn3lU+dJwcCF/CKHv+sowPNSVAAMTBxpGHALiYAJZT4w"
    "GAenwKGQQyakho88hgjmKA4cR4DE4IYIWykUYPQQQJ0RCzJbBvLrN4cRNuEjpMmtd69PEX"
    "TMXJzIFHNLXGdzT2JDzM6koZhtohvECVycGntzZhO8sEaYCdSCGPqAQfF45gcifBFdnGaS"
    "URRpahKFmPEx4RQEDsukuyIHBsGCPx4NlQlaYpb33f2Do4Pjj4cHx9xERrJAjsIovTT3yF"
    "EyMNKUUI4DBiILSWPKm+FDkawOWJm/Uz7CkAuXk5j3LJBpxq4fkositQmRddwmQEpuuqBe"
    "iF2egznGzjwuXA2V2vBqcKOpV19FJi6lD46kSNUGYqQr0XkB3TncFTjh2yHaJIuHdH4Otf"
    "OOuO3cjUcDySChzPLljKmddqeImEDAiI7JTAdmZo0laEIMt0wLG3jmMwub92wL+6aFjYPP"
    "1JWfs/K6VNW+DfyKimZ8CvXkpD2ngo0fey541B2ILWbz2/29vZoC/lCv++fq9Q63KlRlFA"
    "91o7EwR6QHKJ0R39RtQO112Cw5vgylr7ApcqR2e70VSOVWlaTKsTAUPXl6n+kuApgA434G"
    "OEm5kZR9EwEfQVrm/SR2PLu4hg6QKZYpjlXJKX/IfDO5DpNVk6DJXhbkkC6poqs85HbdIg"
    "IwsGTUYm4xU46PJfJtQVS1fssUpFVwrYJrG32r4NrCNqLgGGLOWvJt4bCdQqO3injrVWu3"
    "Xkm68ekYxEu2hQYfKxpGxmVbWKxb8YNbLbfYE7Z2rtTb3dyCvxyPPifmGXb7l+OTAqviLU"
    "FfqwtnPP7fijeD1JfoxiXBm+ewTOAZ8SGy8AWcSx6HPCKAjWVbuvC5bfP4q9K1HPbBbCHr"
    "skuDp8eTgiw65dSbvno6UMLql4QmFfK3gMg4Sgo5GqhVyA/CpBXIrUBudVQrkNvCNieQW3"
    "nXhLzjjNtkiTipfu9IPV6PU0XFBM9dEshGu1lfj9f40NmkhlGhjwx7mYiJR2pVDEhtWhWz"
    "RSrmD/Rp/DF81f2bcdmWQ7GhXxS5c5BvjXUOwch8Owls5MdZZXv+cjMerdueTWSwzt+Og+"
    "iGfjCo4U/kW9+mix25IJXEA07eurGE/wAxRILP"
)
