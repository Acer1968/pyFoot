import sqlite3 as sqlite

path = ''
file = 'save.sqlite'

def make_new_db():
    import os
    try:
        os.remove(path+file)
    except Exception:
        pass
    conn = sqlite.connect(path + file)
    sql = '''CREATE TABLE COMPANY
           (ID      INT         PRIMARY KEY     NOT NULL,
           NAME     TEXT                        NOT NULL,
           AGE      INT                         NOT NULL,
           ADDRESS  CHAR(50),
           SALARY   REAL);
           '''
    conn.execute(sql)
    conn.close()