import sqlite3 as sqlite
import datetime

path = ''
file = 'save.sqlite'

def make_new_db():
    import os
    from data.scripts import db_tables_populate_scripts, db_tables_create_scripts
    try:
        os.remove(path+file)
    except Exception:
        pass
    conn = sqlite.connect(path + file)
    for table in db_tables_create_scripts:  # Create the tables
        conn.execute(db_tables_create_scripts[table])
    for table in db_tables_populate_scripts:  # Populate the new tables
        conn.execute(db_tables_populate_scripts[table])
    conn.close()


