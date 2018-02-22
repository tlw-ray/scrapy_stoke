# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class ScrapyStokePipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['stoke']
        self.collection = self.db['sz']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item