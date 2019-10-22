# -*- coding: utf-8 -*-
import scrapy
from news.items import NewsItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.ss.uestc.edu.cn']
    start_urls = ['http://www.ss.uestc.edu.cn',]
    lis = []
    i = 0
    j = 0
    def parse(self, response):
        basedomain = 'http://www.ss.uestc.edu.cn/'
        url1 = response.xpath('//html/body/div[6]/div/div[2]/div[1]/div[2]/ul[2]/li[5]/ul/li[17]/div/a/@href').get()
        url2 = response.xpath('//html/body/div[6]/div/div[2]/div[1]/div[2]/ul[2]/li[6]/ul/li[17]/div/a/@href').get()
        R1_url1 = basedomain + url1
        R2_url2 = basedomain + url2
        yield scrapy.Request(url = R1_url1, callback = self.getlinks_1)
   #     yield scrapy.Request(url = R2_url2, callback = self.getlinks_2)
        
        
            
        
    def getlinks_1(self, response):
         basedomain = 'http://www.ss.uestc.edu.cn/'
         SpiderSpider.lis = SpiderSpider.lis + response.xpath('//html/body/div[6]/div/div[1]/div/div[2]/article/ul/li')
         urllist = ['']
         urllist[0] = response.xpath('//ul[@class = "pagination-item"]/li[last()]/a/@href').get()
         if SpiderSpider.i < 10:
             for url in urllist:
                 url2 = basedomain + url
                 yield scrapy.Request(url2, callback=self.getlinks_1)
             SpiderSpider.i = SpiderSpider.i + 1
         
         for li in SpiderSpider.lis:
             R_url = basedomain + li.xpath('.//a/@href').get()
             yield scrapy.Request(R_url, callback=self.get_news_1)
             SpiderSpider.lis = []
        
    #def getlinks_2(self, response):
    #    basedomain = 'http://www.ss.uestc.edu.cn/'
    #    SpiderSpider.lis = SpiderSpider.lis + response.xpath('//html/body/div[6]/div/div[1]/div/div[2]/article/ul/li')
    #    urllist = ['']
    #    urllist[0] = response.xpath('//ul[@class = "pagination-item"]/li[last()]/a/@href').get()
    #    if SpiderSpider.j < 10:
    #        for url in urllist:
    #            url2 = basedomain + url
    #            yield scrapy.Request(url2, callback=self.getlinks_2)
    #        SpiderSpider.j = SpiderSpider.j + 1
    #    
    #    for li in SpiderSpider.lis:
    #        R_url = basedomain + li.xpath('.//a/@href').get()
    #        yield scrapy.Request(R_url, callback=self.get_news_2)
    #        SpiderSpider.lis = []
        
    def get_news_1(self, response):
        title1 = response.xpath("//div[@class='key']/div[@class='headline']/h3/text()").get()
        content1 = response.xpath("//div[@class='key']/div[@class='text']/p/text()").getall()
        content1 = "".join(content1)
        item = {"title1":title1, "content1":content1}
        yield item
        
    def get_news_2(self, response):
        title2 = response.xpath("//div[@class='key']/div[@class='headline']/h3/text()").get()
        content2 = response.xpath("//div[@class='key']/div[@class='text']/p/text()").getall()
        content2 = "".join(content2)
        item = {"title2":title2, "content2":content2}
        yield item
        
