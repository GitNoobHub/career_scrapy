# -*- coding: utf-8 -*-
import scrapy
from career.items import CareerItem

#pattern = re.compile("[\u4e00-\u9fa5]")
#pattern2 = re.compile('<!--.*-->')

class CareerspiderSpider(scrapy.Spider):
    name = 'careerspider'
    allowed_domains = ['xkkm.sdzk.cn']
    start_urls = ['http://xkkm.sdzk.cn/zy-manager-web/html/xx.html']

    def parse(self, response):
        
        school_list = response.xpath('//tbody[@class="scrollTbody"]')
#        for tr in school_list.xpath('./tr')[-1::-1]:
        for tr in school_list.xpath('./tr'):
            item = CareerItem()
            item['region'] = tr.xpath('./td[2]/text()').extract()[0]
            item['identify'] = tr.xpath('./td[3]/text()').extract()[0]
            item['name'] = tr.xpath('./td[4]/text()').extract()[0]
            school_url = tr.xpath('./td[last()]/a/text()').extract()
            if school_url:
                item['school_url'] = school_url[0]
            else:
                item['school_url'] = None
        
            href = tr.xpath('./td[last()-1]/a/@href').extract()[0]
            url = 'http://xkkm.sdzk.cn' + href
            request = scrapy.Request(url,
                            callback=self.parse_2)
            request.meta['item'] = item
            yield request
            
    def parse_2(self, response):
        
        skill_list = response.xpath('//tbody[@style="width:100%;"]')
        for tr in skill_list.xpath('./tr'):
            item = response.meta['item']
            item['level'] = tr.xpath('./td[2]/text()').extract()[0]
            item['cate'] = tr.xpath('./td[3]/text()').extract()[0]
            item['sub'] = tr.xpath('./td[4]/text()').extract()[0]
            item['skill'] = tr.xpath('./td[5]').extract()[0]
            yield item