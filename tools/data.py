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


def is_game():
    isgame = True
    import os.path
    if os.path.isfile(path+file):
        player_name, current_date = get_element(['player_name','current_date'])
        if player_name is None or current_date is None:
            isgame = False
    else:
        isgame = False
    return isgame


def get_element(*wargs):
    try:
        conn = sqlite.connect(path + file)
        resp = []
        if wargs[0].lower() == 'all':
            sql = "SELECT e_value from Game"
            cursor = conn.execute(sql)
            r = None
            for row in cursor:
                r = row[0]
            resp.append(r)
        else:
            for name in wargs:
                sql = "SELECT e_value from Game WHERE e_name = %s" % str(name)
                cursor = conn.execute(sql)
                r = None
                for row in cursor:
                    r = row[0]
                resp.append(r)
        conn.close()
    except Exception as e:
        raise e
    return resp