from database.connection import get_db_connection

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        if not id:
            self.save()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID must be an integer.")
        self._id = value

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?);", (self.name,))
        connection.commit()
        self.id = cursor.lastrowid
        connection.close()

    def articles(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM articles WHERE author_id = ?;
        """, (self.id,))
        rows = cursor.fetchall()
        connection.close()
        return rows

    def magazines(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        SELECT DISTINCT m.* 
        FROM magazines m 
        JOIN articles a ON m.id = a.magazine_id
        WHERE a.author_id = ?;
        """, (self.id,))
        rows = cursor.fetchall()
        connection.close()
        return rows
