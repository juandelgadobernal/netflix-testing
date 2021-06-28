from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WDriver():
    """Logs Class"""

    def __init__(self, chrome_web_driver,url):
        """
        Initialize the class and the attributes of the class
        :param chrome_web_driver: the webdriver [string]
        :param url: the url app [string]
        """
        self.chrome_web_driver = chrome_web_driver
        self.url = url

    def call_chrome_webdriver(self):
        """
       The method fo teh chrome driver and also using the implicit wait
        :return:
        """
        # chromedriver = "/browser-drivers" # - "/usr/local/bin"
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_web_driver,options=chr_options)

        #implicit wait
        self.driver.implicitly_wait(10)

        #get url
        self.driver.get(self.url)

    def quit_chrome_webdriver(self):
        """
        The chrome driver close quite the browser
        :return:
        """
        self.driver.quit()




