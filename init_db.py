import sqlite3

def init_db():
    connection = sqlite3.connect('scenarios.db')
    cursor = connection.cursor()

    # Check if the table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='scenarios'")
    if cursor.fetchone() is None:
        # Create the table
        cursor.execute('''
            CREATE TABLE scenarios (
                id TEXT PRIMARY KEY,
                name TEXT,
                author TEXT,
                description TEXT
            )
        ''')

        # Insert 50 rows of example data
        for i in range(1, 51):
            cursor.execute('''
                INSERT INTO scenarios (id, name, author, description)
                VALUES (?, ?, ?, ?)
            ''', (f'xx{i}', f'yy{i}', 'Carlos Garcia', f'Escenario base {i}'))

        connection.commit()
    connection.close()

if __name__ == '__main__':
    init_db()
