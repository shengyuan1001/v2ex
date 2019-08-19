# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class V2exSpider(scrapy.Spider):
    name = 'v2ex'
    allowed_domains = ['www.v2ex.com']
    start_urls = ['https://www.v2ex.com/?tab=hot']

    def parse(self, response):
        #  解析响应内容
        urls = response.xpath(".//span[@class='item_title']//a/@href").extract()
        for url in urls[:5]:
            #  拼接完整url
            url = "https://www.v2ex.com/" + url
            # 返回详细页面请求
            yield Request(url, self.new_parse)

    def new_parse(self, response):
        data = {}
        """设置标题及内容样式"""
        title = "<h3>{}</h3>".format(response.xpath('.//h1/text()').get())
        text = "<span>{}</span>".format(''.join(response.css('.topic_content p::text').extract()))
        data['title'] = title
        data['text'] = text
        yield data
