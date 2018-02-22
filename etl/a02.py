import pymongo
from datetime import datetime

sz = pymongo.MongoClient().stoke.sz
items = sz.find({'$and': [{'指标名称': '股票平均市盈率'}]})
print(items.count())

with open("out.csv", 'w') as f:
    for item in items:
        item_date = item['日期']
        # string_date = str(type(item_date))
        string_value = str(item['本日数值'])
        if type(item_date) == datetime:
            string_date = datetime.strftime(item['日期'], '%Y-%m-%d')
            f.write(str(string_date) + ", " + string_value + "\n")
            print(str(string_date) + ", " + string_value)
