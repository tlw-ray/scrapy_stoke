# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy_stoke.items import DimensionItem


#深圳市场
class SzstokeSpider(scrapy.Spider):
    name = 'szstoke'
    allowed_domains = ['www.szse.cn']

    # start_urls = ['http://www.szse.cn/']

    def start_requests(self):
        url = 'http://www.szse.cn/szseWeb/FrontController.szse'
        header_data = {"Content-Type": "application/x-www-form-urlencoded"}
        # body = "ACTIONID=7&AJAX=AJAX-TRUE&CATALOGID=1803&TABKEY=tab1&REPORT_ACTION=search&txtQueryDate=2018-02-05"
        # return [scrapy.Request(url, method="POST", headers=header_data, body=body, callback=self.parse)]
        requests = []
        begin = datetime.date(2005, 1, 1)
        end = datetime.date(2018, 1, 1)
        for i in range((end - begin).days + 1):
            day = begin + datetime.timedelta(days=i)
            body = "ACTIONID=7&AJAX=AJAX-TRUE&CATALOGID=1803&TABKEY=tab1&REPORT_ACTION=search&txtQueryDate=" + str(day)
            request = scrapy.Request(url, method="POST", headers=header_data, body=body, callback=self.parse)
            requests.append(request)
        return requests


    def parse(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)//进入命令行调试模式
        date = response.xpath("//input[@name='txtQueryDate']").xpath("@value").extract()
        trs = response.css('#REPORTID_tab1').xpath("tr")
        for tr in trs:
            texts = tr.xpath('td/text()')
            if len(texts) >= 6:
                dimension_item = DimensionItem()
                dimension_item['市场'] = '深圳市场'
                dimension_item['日期'] = date
                dimension_item['指标名称'] = texts[0].extract()
                dimension_item['本日数值'] = texts[1].extract()
                dimension_item['比上日增减'] = texts[2].extract()
                dimension_item['幅度pct'] = texts[3].extract()
                dimension_item['本年最高'] = texts[4].extract()
                dimension_item['最高值日期'] = texts[5].extract()
                yield dimension_item
        pass

