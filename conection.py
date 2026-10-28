from dotenv import load_dotenv
import asyncpg
import os


load_dotenv()

paswprd_db = os.getenv("PASSWORD_DB")

async def connection_db():
    try:
        conn = await asyncpg.connect(
            host="localhost",
            port=5432,
            user="postgres",
            database="library_fsm",
            password=paswprd_db
        )
        return conn
    except Exception as Error:
        print(f"Connection Error: {Error}")
        raise





async def create_table():
    conn = await connection_db()
    try:
        await conn.execute("""
CREATE TABLE IF NOT EXISTS author (
    id SERIAL PRIMARY KEY,
    title varchar(30),
    age INT,
    created_at timestamp DEFAULT now(),
    is_active BOOLEAN DEFAULT true
);

CREATE TABLE IF NOT EXISTS category (
    id SERIAL PRIMARY KEY,
    category_name VARCHAR(30),
    created_at timestamp DEFAULT now(),
    is_active boolean DEFAULT true
);

CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title varchar(30),
    caption varchar(30),
    publisher varchar(20),
    author_id int references author(id),
    category_id int references category(id),
    created_at TIMESTAMP DEFAULT now(),
    is_active boolean DEFAULT true
);;
""")
        print("Table create sucessful")
    except Exception as erorr:
        print("Create table erorr", erorr)
        raise
    finally:
        await conn.close()

