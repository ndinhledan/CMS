from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver #pip install salenium
from selenium.webdriver.common.keys import Keys


class AccountTestCase(LiveServerTestCase):


    def setUp(self):
        self.driver = webdriver.Firefox(executable_path ='C:\\Users\\k\\Downloads\\geckodriver.exe') #download geckodriver
        self.selenium = self.driver

        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/posts/register/')
        
        #find the form element
        first_name = selenium.find_element_by_id('firstname')
        last_name = selenium.find_element_by_id('lastname')
        username = selenium.find_element_by_id('uname')
        email = selenium.find_element_by_id('email')
        password1 = selenium.find_element_by_id('pw1')
        password2 = selenium.find_element_by_id('pw2')

        submit = selenium.find_element_by_name('register')

        #Fill the form with data
        first_name.send_keys('Hello')
        last_name.send_keys('Bye')
        username.send_keys('hellobye')
        email.send_keys('hello@byebye.com')
        password1.send_keys('123456')
        password2.send_keys('123456')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'First Name' in selenium.page_source
        #ssert 'sms sent' in selenium.page_source


    def test_incident(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/posts/incident/')
        #find the form element
        name = selenium.find_element_by_id('Name')
        address = selenium.find_element_by_id('Address')
        postal = selenium.find_element_by_id('Postal')
        description = selenium.find_element_by_id('Description')
        mobile = selenium.find_element_by_id('Mobile')
        asssist = selenium.find_element_by_id('assist')
        Severity = selenium.find_element_by_id('Severity')

        submit = selenium.find_element_by_name('Submit')

        #Fill the form with data
        name.send_keys('Hello')
        address.send_keys('1 Good Avenue ABC')
        postal.send_keys('123456')
        description.send_keys('NEED HELP OMG PLS HELP MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
        mobile.send_keys('98765432')
        asssist.send_keys('died')
        Severity.send_keys('6')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'Name :' in selenium.page_source
