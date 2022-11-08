# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# Если мы собираем данные для страниц разных типов, то
# нужно определить каждый тип как отдельный класс в items.py. 

# Если собираемые объекты Item имеют очень
# большие размеры или если мы захотим перенести в их Item
# дополнительные функции синтаксического анализа, то можно
# разместить каждый такой объект в отдельном файле.

import scrapy

class Article(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    lastUpdated = scrapy.Field()
