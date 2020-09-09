# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:

    product_page = scrapy.Field()
    category_name = scrapy.Field()
    product_name = scrapy.Field()
    product_image = scrapy.Field()
    product_main_price = scrapy.Field()
    product_price = scrapy.Field()
    alt_prod_price = scrapy.Field()
    product_reviews = scrapy.Field()
    product_description = scrapy.Field()
    long_product_description = scrapy.Field()
    from_the_manufacturer = scrapy.Field()
    pass
