# - sqlite3.connect(DB_PATH) — database file open karta hai; file nahi hai toh create karta hai.
# - CREATE TABLE IF NOT EXISTS — servers table banata hai, agar pehle se nahi hai toh.
# - PRIMARY KEY AUTOINCREMENT — har record ko unique ID deta hai.
# - UNIQUE — duplicate server names ko database level par rokta hai.
# - REAL — CPU jaise decimal numbers store karta hai.
# - with — connection ko properly manage karta hai.
import sqlite3
import json
from pathlib import Path


DB_PATH = Path(__file__).parent.parent / "devops.db"


def create_database():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS servers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                status TEXT NOT NULL,
                cpu REAL NOT NULL
            )
        """)


def migrate_servers():
    json_path = Path(__file__).parent.parent / "servers.json"

    with open(json_path, "r", encoding="utf-8") as file:
        servers = json.load(file)

    with sqlite3.connect(DB_PATH) as connection:
        connection.executemany(
            """
            INSERT OR IGNORE INTO servers (name, status, cpu)
            VALUES (:name, :status, :cpu)
            """,
            servers,
        )

    print(f"Migration completed. Read {len(servers)} servers.")


if __name__ == "__main__":
    create_database()
    migrate_servers()


def get_all_servers():
    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row

        rows = connection.execute(
            "SELECT * FROM servers"
        ).fetchall()

        return [dict(row) for row in rows]
