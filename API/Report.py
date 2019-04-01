from SendEmail import Send_email
from TelegramBotAPI import tele
from WeatherAPI import psi,weather
from SQLreader import Num_Of_Case
from TwitterAPI import tweets
import schedule
import time

def MorningReport(location,content_id,postal):
    
    """ sends the morning report """
    
    weather_report = weather('morn',location)
    psi_report = psi(content_id)
    case_report = Num_Of_Case(postal)
    tele_group = tele(postal,'Weather: ' + weather_report + '\nPsi: ' + psi_report + '\nTotal number of cases in the last 24 hours: ' + str(case_report[0]) + '\nThe number of resolved cases: ' + str(case_report[1]))
    tweet = tweets(postal,'The Weather: ' + weather_report + '\nPsi: ' + psi_report + '\nTotal number of cases in the last 24 hours: ' + str(case_report[0]) + '\nThe number of resolved cases: ' + str(case_report[1]))
def PeriodicReport():
    
    """ sends the periodic report """
    postal = ''
    case_report = Num_Of_Case(postal)
    msg = ('Number of active cases : ' + str(Num_Of_Case(postal)[2]) + '\nNumber of closed cases : ' + str(Num_Of_Case(postal)[3]))
    Send_email(msg)
                                                                                                                                                                               
def report():
    
    """ send the reports to the respective places """
    
    schedule.every().day.at('08:00').do(MorningReport,'east-{day}','ContentPlaceHolderTicker_C049_LitValueEast','East')
    schedule.every().day.at('08:00').do(MorningReport,'west-{day}','ContentPlaceHolderTicker_C049_LitValueWest','West')
    schedule.every().day.at('08:00').do(MorningReport,'central-{day}','ContentPlaceHolderTicker_C049_LitValueCentral','Central')
    schedule.every().day.at('08:00').do(MorningReport,'north-{day}','ContentPlaceHolderTicker_C049_LitValueNorth','North')
    schedule.every().day.at('08:00').do(MorningReport,'south-{day}','ContentPlaceHolderTicker_C049_LitValueSouth','South')
    schedule.every(10).seconds.do(PeriodicReport)
    while True:
        schedule.run_pending()
        time.sleep(1)
def main():
    report()

if __name__ == '__main__':
    main();
