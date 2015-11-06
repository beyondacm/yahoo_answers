#encoding : utf-8

import scrapy
import re
from scrapy.selector import Selector
from question.items import QuestionItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider

class QuestionSpider(CrawlSpider):
    name = "question"
    allowed_domains = ['answers.yahoo.com']

    item_count = 0
    close_down = False

    start_urls = [
        "https://answers.yahoo.com/question/index?qid=20151030174840AAFIziF",
    ]

    rules = (
        Rule(LinkExtractor(allow=r"\/question\/index\?qid=[a-zA-Z0-9&=]*"),
            callback = 'parse_question', follow = True),
    )

    def parse_question(self, response):
        
        if self.item_count >= 1000:
            self.close_down = True

        if self.close_down:
            raise CloseSpider(reason = 'Data Finished')

        item = QuestionItem()
        self.get_qid(response, item)
        #self.get_qcontent(response, item)
        self.item_count = self.item_count + 1

        yield item
    
    def get_qid(self, response, item):
        
        qid = response.url.strip().split('/')[-1]
        if qid:
            print "question_id:" + qid
            item['question_id'] = qid






