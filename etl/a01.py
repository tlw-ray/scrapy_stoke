import pymongo
import datetime

fieldName = '本日数值'
sz = pymongo.MongoClient().stoke.sz
array = 4
string = 2
items = sz.find({'$and': [{fieldName: {'$type': 2}}, {'指标名称': '股票平均市盈率'}]})
for item in items:
    item[fieldName] = float(item[fieldName])
    sz.save(item)
