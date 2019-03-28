import sqlite3
from datetime import datetime, timedelta

def Num_Of_Case():
    
    """ returns a tuple of open clases and close cases in the last 24 hours """
    """ change the path to ur own location """ 

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    current_time = datetime.now().strftime('%Y-%m-%d %H')
    previous_time = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H')
    c.execute("SELECT * FROM cms_incident")
    open_case = 0
    close_case = 0
    for row in c.fetchall():
        id_time = (row[1])[:13]
        if(id_time > previous_time) and (id_time < current_time):
            open_case += 1
            close_id = (row[6])
            if(close_id != None):
                close_case += 1
    return(open_case,close_case)    


