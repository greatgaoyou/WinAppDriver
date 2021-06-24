import unittest

from appium import webdriver
from selenium.webdriver.common.keys import Keys


class NotepadTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['app'] = r"C:\Windows\System32\notepad.exe"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_edit(self):
        self.driver.find_element_by_name("Text Editor").send_keys("polyv")
        self.driver.find_element_by_name("File").click()
        self.driver.find_element_by_xpath(
            '//MenuItem[starts-with(@Name, "Save")]').click()
        self.driver.find_element_by_xpath(
            '//Pane[starts-with(@ClassName, "Address Band Root")]').find_element_by_xpath(
            '//ProgressBar[starts-with(@ClassName, "msctls_progress32")]').click()
        self.driver.find_element_by_xpath(
            '//Edit[starts-with(@Name, "Address")]').send_keys(
            r"c:\WinAppDriver" )
        self.driver.find_element_by_xpath(
            '//Edit[starts-with(@Name, "Address")]').send_keys(
            Keys.ENTER)
        self.driver.find_element_by_accessibility_id(
            'FileNameControlHost').send_keys("note_test.txt")
        self.driver.find_element_by_name("Save").click()
		
		
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(NotepadTests)
    unittest.TextTestRunner(verbosity=2).run(suite)