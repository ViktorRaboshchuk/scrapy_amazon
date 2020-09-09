import pandas as pd
import re

path = r'pathto_the_file'

df = pd.read_csv(path)

for i in df.columns:
    df[i] = df[i].str.replace('\n', ' ', regex=True)
    df[i] = df[i].str.replace(', , ,', '', regex=True)
    df[i] = df[i].str.replace(' , ', '', regex=True)
    df[i] = df[i].str.replace('by entering your model number.', '')
    df[i] = df[i].apply(lambda x: str(x).replace('  ', ' '))
    df[i] = df[i].apply(lambda x: str(x).replace('  ', ' '))
    df[i] = df[i].apply(lambda x: str(x).replace('  ', ' '))
    df[i] = df[i].apply(lambda x: str(x).replace('  ', ' '))
    df[i] = df[i].str.strip()

df = df[['product_page', 'category_name', 'product_name',
         'product_main_price', 'alt_prod_price', 'product_price',
         'product_description', 'long_product_description', 'from_the_manufacturer',
         'product_image', 'product_reviews']]

for row, i in df.product_price.iteritems():
    if "$" in i:
        str_list = i.split(' ')
        for st in str_list:
            if "$" in st:
                product_price_val = str(re.findall(r"\b\$?[\d,.]+\b", st)[0])
                df.product_price.iloc[row] = product_price_val
    else:
        product_price_val = 0
        df.product_price.iloc[row] = product_price_val

path = r'path'
df.to_csv(path, encoding='utf-8-sig')