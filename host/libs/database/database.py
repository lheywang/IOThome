# ==================================================================================================
# file :        libs/database/database.py
#
# author :      l.heywang
# date :        18/08/2025
#
# brief :       Provide the postgresql handler to make access easier and SQL-less !
# ==================================================================================================
## Imports
# Default libs
import psycopg2
import time
import os

# Modules
from dotenv import load_dotenv  # type: ignore

# -------------------------------------------------------------------------------------------------
# LINITIALISATION CODE (Runned when import !!)
# -------------------------------------------------------------------------------------------------
# Read file
load_dotenv()

# Fetch variables
DB_ADDR = str(os.getenv("DB_ADDR"))
DB_NAME = str(os.getenv("DB_NAME"))
DB_USER = str(os.getenv("DB_USER"))
DB_PASS = str(os.getenv("DB_PASS"))


# -------------------------------------------------------------------------------------------------
# FUNCTIONS
# -------------------------------------------------------------------------------------------------
def connect_db():
    """Establishes a connection to the PostgreSQL database."""
    return psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        host=DB_ADDR,
        password=DB_PASS,
        port=5432,
    )


def setup_db():
    """
    Creates the device_status table if it doesn't already exist.
    """
    with connect_db() as conn:
        with conn.cursor() as cursor:
            # Create the table
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS public.device_status (
                    name                VARCHAR(255)        PRIMARY KEY,
                    last_seen_timestamp DOUBLE PRECISION    NOT NULL,
                    is_online           BOOLEAN             NOT NULL,
                    ip                  VARCHAR(255)        NOT NULL
                );"""
            )
            conn.commit()

            for name in ["temperature", "player", "speaker", "switch"]:
                cursor.execute(
                    f"INSERT INTO device_status (name, last_seen_timestamp, is_online) VALUES ('{name}', -1, false) ON CONFLICT(name) DO NOTHING"
                )
                conn.commit()


def update_device_status(device_name, is_online):
    """
    Updates or inserts the status for a given device using ON CONFLICT.
    """
    with connect_db() as conn:
        with conn.cursor() as cursor:
            current_time = time.time()
            cursor.execute(
                """
                INSERT INTO device_status (name, last_seen_timestamp, is_online)
                VALUES (%s, %s, %s)
                ON CONFLICT(name) DO UPDATE SET
                    last_seen_timestamp = excluded.last_seen_timestamp,
                    is_online = excluded.is_online
            """,
                (device_name, current_time, is_online),
            )
        conn.commit()


def update_device_bool(device_name, is_online):
    """
    Updates or inserts the status for a given device using ON CONFLICT.
    """
    with connect_db() as conn:
        with conn.cursor() as cursor:
            current_time = time.time()
            cursor.execute(
                """
                INSERT INTO device_status (name, last_seen_timestamp, is_online)
                VALUES (%s, %s, %s)
                ON CONFLICT(name) DO UPDATE SET
                    is_online = excluded.is_online
            """,
                (device_name, current_time, is_online),
            )
        conn.commit()


def get_all_device_status():
    """Retrieves all device statuses from the database."""
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT name, last_seen_timestamp, is_online FROM device_status"
            )
            return cursor.fetchall()
