import urllib3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests as req
from bs4 import BeautifulSoup as bs

from config.environ import Environ


class WebFactory:

    def get_driver(self, option):
        try:
            service = Service(ChromeDriverManager().install())
            if option == "headless":
                driver = webdriver.Chrome(service=service, options=self.headless_option())
                return driver
            else:
                driver = webdriver.Chrome(service=service, options=self.no_headless_option())
                return driver
        except Exception as e:
            print(e)

    def headless_option(self):
        option = Options()  # 옵션 생성
        option.add_argument('user-agent=' + Environ.USER_AGENT)
        option.add_argument('headless')  # 브라우저가 뜨지 않고 실행
        option.add_argument("disable-infobars")
        option.add_argument('disable-gpu')  # gpu 사용 안함
        option.add_argument('incognito')  # 시크릿 모드

    def no_headless_option(self):
        option = Options()  # 옵션 생성
        option.add_argument('user-agent=' + Environ.USER_AGENT)
        option.add_argument('disable-gpu')  # gpu 사용 안함
        option.add_argument('incognito')  # 시크릿 모드

    def get_request(self, url, option):
        soup = self.request_option(url, option)
        return soup

    def request_option(self, url, option):
        if option == "verify":
            urllib3.disable_warnings()
            lxml = req.get(url, verify=False, headers={'User-Agent': Environ.USER_AGENT})
            soup = bs(lxml.content, features='lxml-xml')
            return soup
        else:
            html = req.get(url, headers={'User-Agent': Environ.USER_AGENT})
            soup = bs(html.content, 'html.parser')
            return soup