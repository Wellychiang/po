from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, url, page_title):
        self.url = url
        self.page_title = page_title
        self.driver = webdriver.Chrome('/Users/g45p2k7a8/Downloads/chromedriver')

    def _open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(), '打開頁面失敗' + self.url

    def find_element(self, *args):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(args)).is_displayed()
            return self.driver.find_element_by_xpath(args)
        except:
            return "Can't find the " + str(args) + "'s element"

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.page_title in self.driver.title

    def script(self, src):
        self.driver.execute_script(src)


def tryy():
    a = Base('https://developer.aliyun.com/article/364480', 'Selenium的PO模式')
    a.open()
    c = a.find_element("//li//*[contains(text(),'问答')]")
    print(c)


if __name__ == '__main__':
    tryy()