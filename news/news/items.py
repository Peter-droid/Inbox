# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    title1 = scrapy.Field()
    title2 = scrapy.Field()
    content1 = scrapy.Field()
    content2 = scrapy.Field()
    pass
