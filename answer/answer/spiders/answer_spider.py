#encoding : utf-8

import scrapy
import re
from scrapy.selector import Selector
from answer.items import AnswerItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider


class AnswerSpider(scrapy.Spider):
    name = "answers"
    allowed_domains = ['answers.yahoo.com']

    f = open('urls.txt')
    start_urls = [ url.strip() for url in f.readlines() ]
    f.close()
    
    def parse(self, response):
        item = AnswerItem()
        self.get_rid(response, item)
        self.get_vp(response, item)
        self.get_vd(response, item)
        yield item

    def get_rid(self, response, item):
        rid = response.url.strip().split('/')[-1][10:31]
        if rid:
            print rid
            item['related_id'] = rid

    def get_vp(self, response, item):
        vp = response.xpath("//div[@itemprop='upvoteCount']/text()").extract()
        if vp:
            print vp
            item['vote_up'] = vp

    def get_vd(self, response, item):
        vd = response.xpath("//div[@data-ya-type='thumbsDown']/div[1]/text()").extract()
        if vd:
            print vd
            item['vote_down'] = vd

