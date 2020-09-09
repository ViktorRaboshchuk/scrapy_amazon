import scrapy
from ..items import TutorialItem
import time

class QuotesSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
      'https://www.amazon.com/Extendable-Sensyne-YouTube-Compatible-Android/dp/B08B3X7NXC/ref=sr_1_14?dchild=1&fst=as%3Aoff&qid=1599639240&rnid=16225009011&s=electronics&sr=1-14',
        'https://www.amazon.com/Projector-Supported-Compatible-Computer-Entertainment/dp/B07Z22X6NC/ref=sr_1_24?dchild=1&fst=as%3Aoff&qid=1599643513&rnid=16225009011&s=electronics&sr=1-24',
        'https://www.amazon.com/AmazonBasics-Letter-Laminating-Pouches-100-pack/dp/B00BWU3HNY/ref=sr_1_24?dchild=1&fst=as%3Aoff&qid=1599644327&refinements=p_72%3A1248880011&rnid=1248877011&s=electronics&sr=1-24'
    ]

    def parse(self, response):

        items = TutorialItem()

        product_page = response.request.url
        category_name = response.css('ul.a-unordered-list.a-horizontal.a-size-small li span a::text').extract()
        product_name = response.css('h1.a-size-large.a-spacing-none span::text').get()
        product_image = response.css('div.imgTagWrapper#imgTagWrapperId img::attr(data-old-hires)').get()
        if response.css('tr#priceblock_saleprice_row td.a-span12 span::text'):
            product_main_price = response.css('span#priceblock_saleprice::text').get()
        elif response.css('tr#priceblock_dealprice_row td.a-span12 span::text'):
            product_main_price = response.css('span#priceblock_dealprice::text').get()
        elif response.css('tr#priceblock_ourprice_row td.a-span12 span::text'):
            product_main_price = response.css('span#priceblock_ourprice::text').get()
        else:
            product_main_price = response.css('div#buyNew_noncbb span::text').get()

        product_price = response.css('div.a-section.a-spacing-small.a-spacing-top-small span.a-declarative a.a-link-normal span::text').extract()
        alt_prod_price = response.css('span.a-size-medium.a-color-price#mbc-price-1::text').get()
        product_reviews = response.css('span.a-icon-alt::text').get()
        product_description = response.css('ul.a-unordered-list.a-vertical.a-spacing-mini span::text').getall()
        long_product_description = response.css('div.a-section.a-spacing-small#productDescription p::text').extract()
        from_the_manufacturer = response.css('div.apm-lefttwothirdswrap.apm-floatleft div.apm-centerthirdcol p::text').extract()

        items['product_page'] = product_page
        items['category_name'] = category_name
        items['product_name'] = product_name
        items['product_image'] = product_image
        items['product_main_price'] = product_main_price
        items['product_price'] = product_price
        items['alt_prod_price'] = alt_prod_price
        items['product_reviews'] = product_reviews
        items['product_description'] = product_description
        items['long_product_description'] = long_product_description
        items['from_the_manufacturer'] = from_the_manufacturer

        yield items


        # if response.css('span.pagnCur::text').get() == 1:
        #     next_page = response.css('a.pagnNext::attr(href)').get()
        # else:
        #     next_page = response.xpath('//li[@class = "a-last"]/a/@href').extract()[0]
        #
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)


    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').get(),
    #             'author': quote.css('small.author::text').get(),
    #             'tags': quote.css('div.tags a.tag::text').getall(),
    #         }
    #     next_page = response.css('li.next a::attr(href)').get()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)