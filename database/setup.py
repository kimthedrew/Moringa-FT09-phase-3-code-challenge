from connection import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    # Authors Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
    """)

    # Magazines Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    );
    """)

    # Articles Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER,
        magazine_id INTEGER,
        FOREIGN KEY(author_id) REFERENCES authors(id),
        FOREIGN KEY(magazine_id) REFERENCES magazines(id)
    );
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
