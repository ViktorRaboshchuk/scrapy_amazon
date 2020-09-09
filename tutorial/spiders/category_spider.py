import scrapy
from ..items import TutorialItem



class QuotesSpider(scrapy.Spider):
    name = "cat_amazon"
    start_urls = [
        'https://www.amazon.com/b/ref=AE_HP_leftnav_electronics?_encoding=UTF8&ie=UTF8&node=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=WPQ0ATPRBS7BZC61MGAS&pf_rd_r=WPQ0ATPRBS7BZC61MGAS&pf_rd_t=101&pf_rd_p=f9c8a66f-ffbe-4269-9780-afcbe1a37652&pf_rd_p=f9c8a66f-ffbe-4269-9780-afcbe1a37652&pf_rd_i=17938598011'
    ]

    def parse(self, response):

        product_link_categ = response.css('div.a-row.a-expander-container.a-expander-extend-container li span.a-list-item a.a-link-normal.s-ref-text-link::attr(href)').extract()
        for href_categ in product_link_categ:
            yield scrapy.Request(response.urljoin(href_categ), callback=self.parse_list_page)

    def parse_list_page(self, response):

        product_link = response.css('a.a-link-normal.s-no-outline::attr(href)').extract()
        for href in product_link:
            prod_page = response.urljoin(href)
            yield scrapy.Request(prod_page, callback=self.parse_prod_page)

    def parse_prod_page(self, response):

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

        product_price = response.css(
            'div.a-section.a-spacing-small.a-spacing-top-small span.a-declarative a.a-link-normal span::text').extract()
        alt_prod_price = response.css('span.a-size-medium.a-color-price#mbc-price-1::text').get()
        product_reviews = response.css('span.a-icon-alt::text').get()
        product_description = response.css('ul.a-unordered-list.a-vertical.a-spacing-mini span::text').getall()
        long_product_description = response.css('div.a-section.a-spacing-small#productDescription p::text').extract()
        from_the_manufacturer = response.css(
            'div.apm-lefttwothirdswrap.apm-floatleft div.apm-centerthirdcol p::text').extract()

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

        # next_page = response.xpath('//li[@class = "a-last"]/a/@href').extract()[0]
        #
        # if next_page is not None:
        #     yield scrapy.Request(response.urljoin(next_page), callback=self.parse_prod_page)
