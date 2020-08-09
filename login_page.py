from base import Base
from selenium import webdriver

# driver = webdriver.Chrome('/Users/g45p2k7a8/Downloads/chromedriver')
url = 'https://developer.aliyun.com/article/364480'
a = Base(url, 'Selenium的PO模式')
a.open()
# driver.get(url)