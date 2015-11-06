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
        "https://answers.yahoo.com/dir/index?sid=396545469",
        #"https://answers.yahoo.com/question/index?page=1&qid=20120129100259AANhDfd&sort=R",
        #"https://answers.yahoo.com/question/index?qid=20070401213259AA6Sjah&sort=V",
        #"https://answers.yahoo.com/question/index?qid=20080318200319AABBIN6&sort=V",
        #"https://answers.yahoo.com/question/index?qid=20151030174840AAFIziF",
        #"https://answers.yahoo.com/question/index?qid=20130315055034AAIrUJ3&sort=V",
    ]

    rules = (
        Rule(LinkExtractor(allow=r"\/question\/index\?qid=[a-zA-Z0-9&=]*"),
            callback = 'parse_question', follow = True),
    )

    def parse_question(self, response):
        
        if self.item_count >= 2000:
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






