import requests_html
from requests_html import HTMLSession, HTML
import re


class Scraper:
    def run(self, url):
        session = HTMLSession()
        response = session.get(url)

        PageContent = response.html.html

        links = response.html.absolute_links
        print(links)
