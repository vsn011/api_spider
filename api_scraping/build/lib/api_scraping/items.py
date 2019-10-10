# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ApiScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    ober_zeile = scrapy.Field()
    text = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    author = scrapy.Field()
    date_published = scrapy.Field()
    share_url = scrapy.Field()
    comments_number = scrapy.Field()
    shares_facebook = scrapy.Field()
    shares_other = scrapy.Field()
    shares_whatsapp = scrapy.Field()
    shares_total = scrapy.Field()
    thumbs_up = scrapy.Field()
    thumbs_down = scrapy.Field()
    tag = scrapy.Field()
