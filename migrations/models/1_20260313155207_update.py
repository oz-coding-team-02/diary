from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "bookmarks" (
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "id" SERIAL NOT NULL PRIMARY KEY,
    "quote_id" INT NOT NULL REFERENCES "quotes" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_bookmarks_user_id_176fbb" UNIQUE ("user_id", "quote_id")
);
        CREATE TABLE IF NOT EXISTS "user_questions" (
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "id" SERIAL NOT NULL PRIMARY KEY,
    "question_id" INT NOT NULL REFERENCES "questions" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_user_questi_user_id_140794" UNIQUE ("user_id", "question_id")
);
        CREATE TABLE IF NOT EXISTS "blacklisted_token" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "token_hash" VARCHAR(225) NOT NULL UNIQUE,
    "blacklisted_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
        ALTER TABLE "users" ADD "is_admin" BOOL NOT NULL DEFAULT False;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" DROP COLUMN "is_admin";
        DROP TABLE IF EXISTS "bookmarks";
        DROP TABLE IF EXISTS "user_questions";
        DROP TABLE IF EXISTS "blacklisted_token";"""


MODELS_STATE = (
    "eJztXFtv2zYU/iuGn1JgKxIvaYu92Y6zek3sNlG3okUh0BJjE5ZIR6KaGJ3/+0jqRl1nOV"
    "ImwXyLD8/h5Tvk4XdIKj/7NjGh5b7+7EKn/3vvZx8DG7I/EvJfen2w2cRSLqBgYQlFj2kI"
    "CVi41AEGZcJ7YLmQiUzoGg7aUEQwk2LPsriQGEwR4WUs8jB68KBOyRLSlejIt+9MjLAJn6"
    "Ab/tys9XsELTPRT2TytoVcp9uNkE0xvRKKvLWFbhDLs3GsvNnSFcGRNsKUS5cQQwdQyKun"
    "jse7z3sXDDMckd/TWMXvomRjwnvgWVQa7p4YGARz/FhvXDHAJW/l18HZ+dvzd7+9OX/HVE"
    "RPIsnbnT+8eOy+oUBgpvV3ohxQ4GsIGGPcDAfyweqAZvG7ZCUU2TAfxKRlCkwzMH0d/pGG"
    "NgSyDNtQEIMbT6ia0GVjMOfY2gaOK4FSm95M7rThzUc+Ett1HywB0VCb8JKBkG5T0pM3r7"
    "icsOXgL5Kokt7fU+19j//sfZ3PJgJB4tKlI1qM9bSvfd4n4FGiY/KoA1OaY6E0BIZpxo71"
    "NuaBjk1aKsf+r44NOi/5lcVZaANkZd06XgGnwKWyUcqjDLZDfNh44LPBk25BvKQrHu0uLk"
    "pc+Nfwdvx+eHvCtFJ+mQVFA79sl4ByA1z3kTimvgLuqgqcGcN6IH2BZdE8qMhlc9lGOIvn"
    "iBALAlywJUtmKTQXzK4pOKsylBSeJfCN5vPrREQZTbUUjJ9vRpPbkzOBLlNCFMZ7Nic692"
    "tpy+aCBTDWj4DNu0RJjL2JgIOgmwN9YHj14RZaQIwyi3NA9S5ZJdt2Tt9dOGtCaV6AZNNl"
    "bQNn/UwYRkE1HUbCgQZEP9hOznrl8haeCQlPAj4FVXUMFr56yIAUradskT2w0xKAwVL0mr"
    "fNW0osmJykKVpJxVmTtGJV3qTyJkWvVd6kHNtI3kQRtWAVkh8ZdJPcX5zuwe0vTgupPS9K"
    "MnvWHIU4Z1lo8Klgw5BMuoJi2YyffNESkz1E6+Rm+OVVYsJfz2d/hOoSuuPr+SiFKk/N9U"
    "q7sGTx31txO0CtYzfOZERJDLMAXhEHoiX+ALcCxynrEcBG3pJOHXK3D78iXsvEDniMaJ08"
    "Ndjw2KCgn1OOh3fj4eWkvyvOIptkyJ88IvqRYch+QSlDfuAqiiArgqx4lCLIyrHNEWRF75"
    "qgdwzxFckhJ8V5R2zxcpj2h5jgrU08sdHWkn+cne6TgDCtwgxElB14En7ch8DNcrngADiX"
    "zsWHw2WMTjqNVqROkTq19ytSpxyrSF2rSd1BNCS6gV1s9eiBpLqArZmSRCwth5LIDK6Yki"
    "ToYr2U5Ft0OilOsvrfFUdRHEVtZYqjHKtjMxxFxMVqV2CyyTHdgamLwwNAUxeHNVwcZhZs"
    "DbBFt3/dxU0ORG26cU1kCgXfc+13WidmRoNHdjI/DvqjKLKiyIpJKYp8tI7Noch+aKzKkh"
    "NWx8T5FFFWRLkNRDlmWM/myl089s3S5UREahNjHlmsGgu5DFaNrGEua87olDLnRazNGG+o"
    "ru67Wxb1yoiycFvlz4OTVp383Hqw15fBg5IvgweZL4Pl9VCdoGatFUltQfZR4Vq0yeg9hA"
    "4yVnkxOygpjdQg1lHhuUPh+Qd03Fx6VRybJZOuvG54gX/awJdGBRAD9W4CWNvD1L3e2fx5"
    "N59VfWdjIoP2/unxza6dgJbgx8db/t4m/bQmtQ/xCiq+t6l/Y9n9C3xkzd8="
)
