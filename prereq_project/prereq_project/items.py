# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PrereqProjectItem(scrapy.Item):
    course_name = scrapy.Field()
    url_link = scrapy.Field()
