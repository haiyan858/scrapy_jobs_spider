# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZhilianSpiderSpider(CrawlSpider):
    name = 'zhilian_spider'
    allowed_domains = ['zhaopin.com']
    start_urls = ['file:///var/folders/s0/v_78s7nx6b5dq1c9vt1td_2r0000gn/T/tmpm6tovt2o.html']

    rules = (
        Rule(LinkExtractor(allow=r'http://jobs\.zhaopin\.com/.*\.htm'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        i = {}
        i = {}
        # 岗位名称
        i['job_name'] = response.xpath('//div[@class="cn"]/h1/@title').extract_first()
        # 工作地点
        i['job_area'] = response.xpath('//div[@class="cn"]/span[@class="lname"]/text()').extract_first()
        # 工作薪水
        i['job_price'] = response.xpath('//div[@class="cn"]/strong/text()').extract_first()
        # 公司名称
        i['job_company'] = response.xpath('//div[@class="cn"]/p[@class="cname"]/a/@title').extract_first()
        # 公司概况
        i['job_company_abstract'] = response.xpath('//div[@class="cn"]/p[@class="msg ltype"]/text()').extract_first()
        # 工作岗位所在页面的链接
        i['job_url'] = response.url
        i['flag'] = "智联招聘"
        print(i)
        # return i
