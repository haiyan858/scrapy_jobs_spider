# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QianchengSpiderSpider(CrawlSpider):
    name = 'qiancheng_spider'
    allowed_domains = ['51job.com']
    start_urls = ['http://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html']

    rules = (
        Rule(LinkExtractor(allow=r'http://jobs\.51job\.com/beijing-.*?/\d+\.html.*'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
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
        i['flag'] = "前程无忧"
        # print(i)
        # {
        # 'job_name': 'Python开发工程师',
        # 'job_area': '北京-朝阳区',
        # 'job_price': '0.8-1万/月',
        # 'job_company': 'NTT DATA（中国）有限公司',
        # 'job_company_abstract': '\r\n\t\t\t\t外t\t\xa0\xa0|\xa0\xa0500-1000人    \t\t    \t\t    \t\t\t\xa0\xa0|\xa0\xa0计算机软件    \t\t\t\t\t',
        # 'job_url': 'http://jobs.51job.com/beijing-cyq/95927068.html?s=01&t=0'
        # 'flag': '前程无忧'
        # }

        return i
