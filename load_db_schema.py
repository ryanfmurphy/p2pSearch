import sqlite3

db = sqlite3.connect('urls.db')
with open('db_schema.sql','r') as fh:
    db_schema_sql = fh.read()
    db.executescript(db_schema_sql)
    db.commit()

db.close()

