from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_ask_user_to_browse_for_file(self):
        # Ram goes to check the homepage of the new website
        self.browser.get('http://localhost:8000')

        # He notices the title of the browser tab
        self.assertIn('Kingdom in Django', self.browser.title)
        self.fail('You hit the simulated failure.')
        
        # Ram is then invited to browse for a specially structured .txt file

        # The button text changes from 'Browse' to 'Upload' after selecting the file

        # Ram then clicks the button to upload the file. After the successful file upload, he is
        # taken to a new page which shows the processed stats of the file

if __name__ == '__main__':
    unittest.main(warnings='ignore')
