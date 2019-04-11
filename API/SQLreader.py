import sqlite3
from datetime import datetime, timedelta

def Num_Of_Case(postal):
    
    """ returns a tuple of open clases and close cases in the last 24 hours """
    """ change the path to ur own location """
    
    North = frozenset(["No","28","29","30","31","32","33","34","35","36","37","53","54","55","56","57","72","73","75","76","77","78","79","80","82"])
    West = frozenset(["We","60","61","62","63","64","65","66","67","68","69","70","71"])
    East = frozenset(["Ea","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","81"])
    Central = frozenset(["Ce","01","02","03","04","05","06","07","08","18","19","20","21","22","23","24","25","26","27","58","59"])
    South = frozenset(["So","09","10","11","12","13","14","15","16","17"])

    
    conn = sqlite3.connect('C:\\Users\\VMadmin\\Downloads\\CMS-FrontEndKKS\\CMS-FrontEndKKS\\db.sqlite3')
    c = conn.cursor()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    previous_time = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M')
    c.execute("SELECT * FROM cms_incident")
    open_case = close_case =  open_case_all = close_case_all = 0
    for row in c.fetchall():
        location = (row[4])
        if location[-6:-4] in North and postal[:2] in North:
            id_time = (row[2])[:16]
            if(id_time > previous_time) and (id_time < current_time):
                open_case += 1
                close_id = (row[7])
                if(close_id != None):
                    close_case += 1
                    open_case -= 1
        if location[-6:-4] in South and postal[:2] in South:
            id_time = (row[2])[:16]
            if(id_time > previous_time) and (id_time < current_time):
                open_case += 1
                close_id = (row[7])
                if(close_id != None):
                    close_case += 1
                    open_case -= 1
        if location[-6:-4] in East and postal[:2] in East:
            id_time = (row[2])[:16]
            if(id_time > previous_time) and (id_time < current_time):
                open_case += 1
                close_id = (row[7])
                if(close_id != None):
                    close_case += 1
                    open_case -= 1
        if location[-6:-4] in West and postal[:2] in West:
            id_time = (row[2])[:16]
            if(id_time > previous_time) and (id_time < current_time):
                open_case += 1
                close_id = (row[7])
                if(close_id != None):
                    close_case += 1
                    open_case -= 1
        if location[-6:-4] in Central and postal[:2] in Central:
            id_time = (row[2])[:16]
            if(id_time > previous_time) and (id_time < current_time):
                open_case += 1
                close_id = (row[7])
                if(close_id != None):
                    close_case += 1
                    open_case -= 1
    c.execute("SELECT * FROM cms_incident")
    for row in c.fetchall():
        id_time = (row[2])[:16]
        close_id = (row[7])
        if(close_id != None):
            if(id_time > previous_time) and (id_time < current_time):
                close_case_all += 1
        else:
            open_case_all += 1
    return(open_case,close_case,open_case_all,close_case_all)

print(Num_Of_Case(''))
