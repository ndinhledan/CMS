from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

""" Change the path to your own location and change the source code for webdriver
    so that the command prompt doesnt pop up
    I copied instructions from:
    https://stackoverflow.com/questions/48654427/hide-command-prompt-in-selenium-chromedriver """

path = r'chromedriver.exe'
options = Options()
options.headless = True
args = ['hide_console']
driver = webdriver.Chrome(executable_path=path,chrome_options=options,service_args=args)
    
def all_psi():
    
     """ This function returns the 24 hr PSI and returns the PSI as a string """

     url = 'https://www.nea.gov.sg'
     page_source = driver.get(url)
     source = driver.page_source
     soup = BeautifulSoup(source,'html.parser')
     psi_level = soup.find_all('div',class_='number')[0].text
     print('(ALL)The 24 hr PSI is ' + psi_level)

def psi(content_id):
    
    """ This function takes in a string:
    ContentPlaceHolderTicker_C049_LitValueNorth/South/East/Central/West
    and returns a the PSI value as a string """
    url2 = 'https://www.haze.gov.sg/'
    page_source = driver.get(url2)
    source = driver.page_source
    soup2 = BeautifulSoup(source, 'html.parser')
    psi_all = soup2.find_all('div',class_='top')
    for psi in psi_all:
        psi = psi.find_all('span',{'id':content_id})
        if (len(psi)>0 ):
            result = psi[0].text
            return result

def weather(time,location):
    
    """ This function takes in the a string for the time (morn/afternoon/nextnight) and
    location (north-{day}/south/east/west/central) and returns the
    weather at the location as a string  """

    url3 = 'https://www.nea.gov.sg/weather'
    page_source = driver.get(url3)
    source = driver.page_source
    soup3 = BeautifulSoup(source,'html.parser')
    weather_all = soup3.find_all('div',{'data-day':time})
    for weather1 in weather_all:
        weather1 = weather1.find_all('span',{'id':location})
        if(len(weather1)>0):
            result = weather1[0]['title']
            return result

""" example of functions """
#all_psi()
#psi_north = psi('ContentPlaceHolderTicker_C049_LitValueNorth')
#weather_north = weather('morn','north-{day}')
#print('(NORTH)Weather is '+weather_north+ ' and PSI is '+psi_north)




