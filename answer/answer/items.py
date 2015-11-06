# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnswerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    related_id = scrapy.Field()
    vote_up = scrapy.Field()
    vote_down = scrapy.Field()

    #pass
