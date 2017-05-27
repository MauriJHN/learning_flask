import sqlite3

def start_database():
    conn = sqlite3.connect('database.db', timeout=None, isolation_level=None, detect_types=None, factory=None)

def submit(sql):
    conn = sqlite3.connect('database.db', timeout=None, isolation_level=None, detect_types=None, factory=None)
    cursor = conn.cursor()
    cursor.execute(sql)
    # save the changes to the database
    conn.commit()
    # close the database
    conn.close()
