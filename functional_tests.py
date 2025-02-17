## python3 functional_tests.py firefox eve.ii.pw.edu.pl 9007

# -*- coding=utf-8 -*-
"""functional testing for dnaasm web application"""

import sys
import os
import time
import unittest
import splinter
from splinter import Browser
from splinter.exceptions import DriverNotFoundError
import time
localtime = time.localtime(time.time())
date_today = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[0:10])

## @brief test-cases
class TestFunctionalDnaasm(unittest.TestCase):
    
    ## Browser used for testing - default Google Chrome
    browser = ''
    admin_user = ''
    admin_user_password = ''

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        self.browser.reload()
        pass

    def tearDown(self):
        try:
            alert = self.browser.get_alert()
            alert.accept()
        except:
            pass

    def clickCssLink(self, ident, interval=0.1, maxTime=2):
        """Searches for an css and clicks it"""
        browser = self.browser
        counter = 0
        link = None
        while counter < maxTime:
            try:
                browser.find_by_css(ident).first.click()
                return
            except:
                time.sleep(interval)
                counter += interval
        link = browser.find_by_css(ident)
        self.assertGreaterEqual(len(link), 1, "Cannot find link with ident='{css}' in {brow}".format(css=ident, brow = 'browser'))
        link.first.click()

    def clickIdLink(self, ident, interval=0.1, maxTime=2):
        """Searches for an identifier and clicks it"""
        browser = self.browser
        counter = 0
        link = None
        while counter < maxTime:
            try:
                browser.find_by_id(ident).first.click()
                return

            except:
                time.sleep(interval)
                counter += interval
        link = browser.find_by_id(ident)
        self.assertGreaterEqual(len(link), 1, "Cannot find link with ident='{css}' in {brow}".format(css=ident, brow = 'browser'))
        link.first.click()

    def waitForElement(self, ident, interval=0.1, maxTime=2):
        """Waits for element"""
        browser = self.browser
        counter = 0
        while counter < maxTime:
            counter += interval
            time.sleep(interval)
            if browser.is_element_present_by_id(ident):
                return

    def test01AnyAnswer(self):
        """tests if the application is loaded"""
        self.assertTrue(len(self.browser.html) > 0)
		
    def test02ProperTitle(self):
        """tests if the web page title is correct"""
        title = self.browser.title
        if not isinstance(title, str):
            title = title.decode()
        self.assertEqual(title, 'DnaAssembler')

    def test03TestHelpPagePL(self):
        """tests Help Page PL"""
        self.browser.reload()
        self.clickCssLink('#showHelpWindowButton')
        self.clickCssLink('#a_lang_pl')
        self.assertEqual(len(self.browser.find_by_text(u"DnaAssembler - Pomoc")), 1)
        self.assertEqual(self.browser.find_by_id('showHelpWindowButton').first.text, u'Pomoc')
        self.assertEqual(self.browser.find_by_id('showHelpWindowButton').first['title'], u"Kliknij, aby zobaczyć pomoc dla aplikacji")
        self.assertEqual(self.browser.find_by_id('loginAsGuestButton').first.text, u'Zaloguj się jako gość')
        self.assertEqual(self.browser.find_by_id('loginAsGuestButton').first['title'], u"Kliknij, aby zalogować się do aplikacji jako gość")
        self.assertEqual(self.browser.find_by_id('showLoginWindowButton').first.text, u'Zaloguj się')
        self.assertEqual(self.browser.find_by_id('showLoginWindowButton').first['title'], u"Kliknij, aby zalogować się do aplikacji")
        self.assertEqual(self.browser.find_by_id('showNewUserWindowButton').first.text, u'Dodaj użytkownika')
        self.assertEqual(self.browser.find_by_id('showNewUserWindowButton').first['title'], u"Kliknij, aby dodać nowego użytkownika")
        self.assertEqual(self.browser.find_by_id('a_lang_en').first['title'], u"Kliknij, aby zmienić język na angielski")
        self.assertEqual(self.browser.find_by_id('a_lang_pl').first['title'], u"Kliknij, aby zmienić język na polski")
        self.assertEqual(len(self.browser.find_by_text(u"Formaty plików wejściowych i wyjściowych")), 1)
        self.assertEqual(self.browser.find_by_text(u"Formaty plików wejściowych i wyjściowych").first['title'], u"Kliknij, aby zobaczyć opis formatów plików wejściowych akceptowanych przez aplikację i opis formatów plików wyjściowych produkowanych przez aplikację")
        self.assertEqual(len(self.browser.find_by_text(u"Parametry i algorytmy wykorzystane w aplikacji")), 1)
        self.assertEqual(self.browser.find_by_text(u"Parametry i algorytmy wykorzystane w aplikacji").first['title'], u"Kliknij, aby zobaczyć opis parametrów i algorytmów wykorzystanych w aplikacji")
        self.assertEqual(len(self.browser.find_by_text(u"Uzyskaj więcej informacji wysyłając wiadomość:")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"r.m.nowak@elka.pw.edu.pl")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Autorzy")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Robert Nowak - r.m.nowak@elka.pw.edu.pl")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Wiktor Kuśmirek")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Politechnika Warszawska,")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Wydział Elektroniki i Technik Informacyjnych,")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Warszawa 2015")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Parametry aplikacji")), 1)
        self.assertEqual(((self.browser.find_by_id('server_time').first.text))[0:13], u"czas serwera:")
        self.assertEqual(((self.browser.find_by_id('server_time_val').first.text)[0:10]), date_today)
        self.assertEqual((self.browser.find_by_id('db_version').first.text)[0:19], u"wersja bazy danych:")
        self.assertEqual(self.browser.find_by_id('db_version_val').first.text, u"PostgreSQL 9.4.18 on x86_64-unknown-linux-gnu")
        self.assertEqual((self.browser.find_by_id('server_version').first.text)[0:15], u"wersja serwera:")
        self.assertEqual(self.browser.find_by_id('server_version_val').first.text, u"0.07.1635; Python: 3.5.3; Arch: ; Os: Linux #1 SMP Debian 4.9.110-1 (2018-07-05); Django: 2.0.2")
        self.assertEqual((self.browser.find_by_id('client_version').first.text)[0:15], u"wersja klienta:")
        self.assertEqual(self.browser.find_by_id('client_version_val').first.text, u"0.06.1634")


        
    def test04TestHelpPageEN(self):
        """tests Help Page EN"""
        self.clickCssLink('#a_lang_en')
        self.assertEqual(len(self.browser.find_by_text(u'DnaAssembler - Help')), 1)
        self.assertEqual(self.browser.find_by_id('showHelpWindowButton').first.text, u'Help')
        self.assertEqual(self.browser.find_by_id('showHelpWindowButton').first['title'], u"Click to view help page")
        self.assertEqual(self.browser.find_by_id('loginAsGuestButton').first.text, u'Log in as guest')
        self.assertEqual(self.browser.find_by_id('loginAsGuestButton').first['title'], u"Click to log in as guest")
        self.assertEqual(self.browser.find_by_id('showLoginWindowButton').first.text, u'Log in')
        self.assertEqual(self.browser.find_by_id('showLoginWindowButton').first['title'], u"Click to log in")
        self.assertEqual(self.browser.find_by_id('showNewUserWindowButton').first.text, u'Create new user')
        self.assertEqual(self.browser.find_by_id('showNewUserWindowButton').first['title'], u"Click to create new user")
        self.assertEqual(self.browser.find_by_id('a_lang_en').first['title'], u"Click to change language to english")
        self.assertEqual(self.browser.find_by_id('a_lang_pl').first['title'], u"Click to change language to polish")
        self.assertEqual(len(self.browser.find_by_text(u"Input and output file formats")), 1)
        self.assertEqual(self.browser.find_by_text(u"Input and output file formats").first['title'], u"Click to view description of input file formats accepted by application and output file formats produced by application")
        self.assertEqual(len(self.browser.find_by_text(u"Parameters and algorithms used in application")), 1)
        self.assertEqual(self.browser.find_by_text(u"Parameters and algorithms used in application").first['title'], u"Click to view description of parameters and algorithms used in application")
        self.assertEqual(len(self.browser.find_by_text(u"For more information send an email:")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"r.m.nowak@elka.pw.edu.pl")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Robert Nowak - r.m.nowak@elka.pw.edu.pl")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Wiktor Kuśmirek")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Warsaw University of Technology,")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Faculty of Electronics and Information Technology,")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"Warsaw 2015")), 1)
        self.assertEqual(len(self.browser.find_by_text(u"server time: ")), 1)
        self.assertEqual(((self.browser.find_by_id('server_time').first.text))[0:12], u"server time:")
        self.assertEqual(((self.browser.find_by_id('server_time_val').first.text)[0:10]), date_today)
        self.assertEqual((self.browser.find_by_id('db_version').first.text)[0:11], u"db version:")
        self.assertEqual(self.browser.find_by_id('db_version_val').first.text, u"PostgreSQL 9.4.18 on x86_64-unknown-linux-gnu")
        self.assertEqual((self.browser.find_by_id('server_version').first.text)[0:15], u"server version:")
        self.assertEqual(self.browser.find_by_id('server_version_val').first.text, u"0.07.1635; Python: 3.5.3; Arch: ; Os: Linux #1 SMP Debian 4.9.110-1 (2018-07-05); Django: 2.0.2")
        self.assertEqual((self.browser.find_by_id('client_version').first.text)[0:15], u"client version:")
        self.assertEqual(self.browser.find_by_id('client_version_val').first.text, u"0.06.1634")
   
if __name__ == "__main__":
    www_browser = sys.argv[1] if len(sys.argv) >= 2 else 'chrome'
    www_addr = sys.argv[2] if len(sys.argv) >= 3 else '127.0.0.1'
    www_port = sys.argv[3] if len(sys.argv) >= 4 else '9000'
    admin_user = sys.argv[4] if len(sys.argv) >= 5 else ''
    admin_user_password = sys.argv[5] if len(sys.argv) >= 6 else ''

    browser = None

    try:
        if www_browser == 'firefox':
            caps = {}
            caps['acceptInsecureCerts'] = True
            browser = Browser('firefox', capabilities=caps)
        else:
            browser = Browser(www_browser)
    except DriverNotFoundError:
        print("ERROR: WebDriver for browser '" + www_browser  + "' not found.")

    browser.driver.maximize_window()

    print('http://' + www_addr + ':' + www_port)

    browser.visit('http://' + www_addr + ':' + www_port)

    TestFunctionalDnaasm.browser = browser
    TestFunctionalDnaasm.admin_user = admin_user
    TestFunctionalDnaasm.admin_user_password = admin_user_password

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFunctionalDnaasm))

    testToRun = 'all'

    if testToRun != 'all':
        anyTestWillBeRun = False

        for ts in suite:
            for t in ts:
                if testToRun not in t.id():
                    setattr(t, 'setUp', lambda: t.skipTest('Not running this time'))
                else:
                    anyTestWillBeRun = True
        if not anyTestWillBeRun:
            print('ERROR: Cannot run given test because it doesn\'t exist: ' + testToRun)
            sys.exit()

    try:
        from xmlrunner import XMLTestRunner
        if not os.path.exists('./reports'):
            os.makedirs('./reports')
        with open('./reports/functional_output.xml', 'w') as output:
            XMLTestRunner(output=output, verbosity=3).run(suite)

    except ImportError:
        print("Failed to import xmlrunner library. Using TextTestRunner instead...\n\n")
        unittest.TextTestRunner(verbosity=3).run(suite)

    browser.quit()
