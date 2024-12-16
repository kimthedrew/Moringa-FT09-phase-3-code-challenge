from database.connection import get_db_connection

def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()


    cursor.execute('DROP TABLE IF EXISTS articles')
    cursor.execute('DROP TABLE IF EXISTS magazines')
    cursor.execute('DROP TABLE IF EXISTS authors')

    # Authors Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """)

    # Magazines Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    );
    """)

    # Articles Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,           
        author_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        FOREIGN KEY(author_id) REFERENCES authors(id),
        FOREIGN KEY(magazine_id) REFERENCES magazines(id)
    );
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
