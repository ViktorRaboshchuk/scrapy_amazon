# scrapy_amazon

In this project I parsed Amazon Electronics category using python Scrapy package. Output is CSV file with such columns:

	product_page - web link to the product 
	category_name - sub Electrinics category
    product_name - title of the product
    (there are several price objects on the page that may not be displayed, so I parsed price from different places)
    product_main_price - price#1
    alt_prod_price - price#2
    product_price - price#3
    product_description - short description of the product at the begining of the page
    long_product_description - long description of the product at the end of the page(may not be displayed)
    from_the_manufacturer - some description from manufacturer
    product_image - main image of the product
    product_reviews - start count(reviews)
    
In the main scraper you cood uncomment code to fetch all product from each sum category.

Also you can find python file with data processing. Sample code prettifying dataframe columns.

