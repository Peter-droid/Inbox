# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class NewsPipeline(object):
    def __init__(self):
        dbparams = {
                'host': '127.0.0.1',
                'port': 3306,
                'user': 'root',
                'password': 'lx123,.,.',
                'database': 'news',
                'charset': 'utf8'
                }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql1 = None
        self._sql2 = None
    def open_spider(self, spider):
        print("开始")
    
    
    def process_item(self,item,spider):
        self.cursor.execute(self.sql1, (item['title1'], item['content1']))
        self.conn.commit()
        return item
    
    #def process_item(self,item,spider):
    #    self.cursor.execute(self.sql2, (item['title2'], item['content2']))
    #    self.conn.commit()
    #    return item
    
    @property
    def sql1(self):
        if not self._sql1:
            self._sql1 = """
            insert into teachers(id,title,content) values(null,%s,%s)
            """
            return self._sql1
        return self._sql1
    @property
    def sql2(self):
        if not self._sql2:
            self._sql2 = """
            insert into students(id,title,content) values(null,%s,%s)
            """
            return self._sql2
        return self._sql2
    
    def close_spider(self, spider):
        print("结束")
