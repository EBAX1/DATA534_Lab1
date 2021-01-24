import scrapy
import html5lib
from bs4 import BeautifulSoup


class MySpider(scrapy.Spider):

    name = "mySpider"
    allowed_domains = ["ubc.ca"]
    start_urls = [
        "https://courses.students.ubc.ca/cs/courseschedule?tname=subj-department&campuscd=UBCO&dept=DATA&pname=subjarea"
    ]
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    }

    def __init__(self):
    	self.log_file = open('log_file', 'w')

    def parse(self, response):
      soup = BeautifulSoup(response.text)
      table = soup.find("table")

      for entry in table.find_all("a"):
          course = items.PrereqProjectItem()
          course["course_name"] = entry.text
          course["url_link"] = entry["href"]

      return

    def parse_course_details(self, response):
    	pass