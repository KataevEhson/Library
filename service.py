from conection import connection_db


async def create_author(name, age):
    try:
        conn = await connection_db()
        await conn.execute("""
            INSERT INTO author (title, age) VALUES
            ($1, $2)
        """, name, age)
    except Exception as erorr:
        print("Create book author!!!")
    finally:
        await conn.close()


async def create_book_for_me(title, caption, publisher, author_id, category_id):
    try:
        conn = await connection_db()
        await conn.execute("""
            INSERT INTO books (title, caption, publisher, author_id, category_id) VALUES
            ($1, $2, $3, $4, $5)
        """, title, caption, publisher, author_id, category_id)
    except Exception as erorr:
        print("Create book erorr!!!")
    finally:
        await conn.close()


async def create_category_for_me(category_name):
    try:
        conn = await connection_db()
        await conn.execute("""
            INSERT INTO category (category_name) VALUES
            ($1)
        """, category_name)
    except Exception as erorr:
        print("Create book category!!!")
    finally:
        await conn.close()








async def update_book_for_me(title, caption, publisher, book_id):
    try:
        conn = await connection_db()
        await conn.execute("""
UPDATE books
SET title = $1,
caption = $2,
publisher = $3
WHERE id = $4
""", title, caption, publisher, book_id)
    except Exception as erorr:
        print("Update book erorr:", erorr)
    finally:
        await conn.close()















async def delete_book(book_id):
    try:
        conn = await connection_db()
        await conn.execute("""
    DELETE FROM books
    WHERE id = $1
            """,book_id)
    except Exception as erorr:
        print("Delete erorr:", erorr)
    finally:
        await conn.close()







async def seek_book(book_id):
    try:
        conn = await connection_db()
        a = await conn.fetch("""
SELECT * FROM books
WHERE id = $1
""", book_id)
        return a

    except Exception as erorr:
        print("Seek book erorr:", erorr)
    finally:
        await conn.close()





async def get_all_books():
    try:
        conn = await connection_db()
        a = await conn.fetch("""
SELECT * FROM books

""")
        return a
    except Exception as erorr:
        print("Seek books erorr:", erorr)
    finally:
        await conn.close()


async def seek_books_by_author(author_id):
    try:
        conn = await connection_db()
        a = await conn.fetch("""
SELECT * FROM books
WHERE author_id = $1
""", author_id)
        return a
    except Exception as erorr:
        print("Seek books erorr:", erorr)
    finally:
        await conn.close()


async def seek_books_by_category(category_id):
    try:
        conn = await connection_db()
        a = await conn.fetch("""
SELECT * FROM books
WHERE category_id = $1
""", category_id)
        return a
    except Exception as erorr:
        print("Seek books erorr:", erorr)
    finally:
        await conn.close()
