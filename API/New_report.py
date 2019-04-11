import sqlite3
from datetime import datetime, timedelta

def PrimeMinisterReport():

    conn = sqlite3.connect('C:\\Users\\VMadmin\\Downloads\\CMS-FrontEndKKS\\CMS-FrontEndKKS\\db.sqlite3')
    c = conn.cursor()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    previous_time = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M')
    c.execute("SELECT * FROM cms_incident")
    id_number = ''
    time = ''
    location = ''
    incident_type = ''
    assistance_type = ''
    line1 = ''
    for row in c.fetchall():
        id_time = (row[2])[:16]
        if(id_time > previous_time) and (id_time < current_time):
            id_number = str((row[0]))
            time = str((row[2])[:16])
            location = str((row[4]))
            incident_type = str((row[1]))
            if incident_type == 'FIR':
                incident_type= 'Fire'
            elif incident_type == 'HAZ':
                incident_type = 'Haze'
            elif incident_type == 'BIR':
                incident_type = 'Bird Flu Outbreak'
            elif incident_type == 'TSU':
                incident_type = 'Tsunami'
            elif incident_type == 'AFT':
                incident_type = 'Earthquake Aftershock'
            elif incident_type == 'TER':
                incident_type = 'Terrorist Activity'
            assistance_type = str((row[3]))
            if assistance_type == '1':
                assistance_type = 'Rescue and Evacuation'
            elif assistance_type == '1003':
                assistance_type = 'Emergency and Ambulance'
            elif assistance_type == '1004':
                assistance_type = 'Fire Fighting'
            elif assistance_type == '1005':
                assistance_type = 'Gas Leak Control'
            line ="ID: "+id_number+"\nTime: "+time+"\nLocation: "+location+"\nIncident type: "+incident_type+"\nAssistance: "+assistance_type
            line1 += '\n\n' + line
    return line1

