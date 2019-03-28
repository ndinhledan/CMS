import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Send_email(content):
    """ takes in a string and send the emails with the string as the message"""
    msg = MIMEMultipart()
    msg['From'] = 'oneplusninecms@gmail.com'
    msg['To'] = 'kaiz123129@gmail.com'
    msg['Subject'] = 'Update on cases'
    message = content
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('oneplusninecms@gmail.com', 'abcd@1234')
    mailserver.sendmail('oneplusninecms@gmail.com','kaiz123129@gmail.com',msg.as_string())
    mailserver.quit()



