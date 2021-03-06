import logging

DB = {"host":"localhost", "username": "ali", "password": "ali222", "dbname": "ali_upwork", "charset": "utf8", "variants_table": "tbl_aliexpress_variants"}

DDL = """create table if not exists %s(
                product_id bigint,
                product_title varchar(1000),
                product_price varchar(100),
                product_image varchar(2000),
                product_url varchar(2000),
                variant_id varchar(255),
                variant_price decimal(10,2),
                variant_title varchar(1000),
                shipping_cost decimal(10,2))""" % DB['variants_table']

HTTP_TIMEOUT_SEC = 5

test_urls = ['https://www.aliexpress.com/item/2015-New-sneakers-women-outdoor-sport-shoes-summer-breathable-mesh-running-shoes-white-light-casual-shoes/32319495269.html?spm=2114.01010208.3.11.52x5UF&ws_ab_test=searchweb201556_10,searchweb201602_4_10057_10065_10056_10055_10054_10069_10059_10058_10017_10070_10060_10061_10052_10062_10053_10050_10051,searchweb201603_2&btsid=37c9b998-c074-4778-97f5-e1482f3e2d31',
             'https://www.aliexpress.com/store/product/Woman-Winter-Velvet-Warm-velvet-dress-with-long-sleeves-shift-brieft-Pleat-Knee-Length-Office-work/312854_2052999664.html?spm=a2g01.8005228.0.31.264FrC&sdom=562.108230.97211.0_2052999664',
             'https://www.aliexpress.com/item/Original-Xiaomi-Redmi-Note-4-Mobile-Phone-MTK-Helio-X20-Deca-Core-5-5-inch-OLED/32721716490.html?spm=2114.01010208.3.11.RslV4x&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10065_10068_10055_10054_10069_10059_10058_10073_10017_10070_10060_10061_10052_10062_10053_10050_10051,searchweb201603_4&btsid=ef056dcb-8ec0-4f31-a01a-e3c2692e9b53',
             'https://www.aliexpress.com/item/High-Quality-Casual-Men-s-Hooded-With-Black-Gown-Sudaderas-Hombre-Hip-Hop-Hoodies-and-Sweatshirts/32687892245.html?spm=2114.01010108.3.416.OcwsCs&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10065_10068_10055_10054_10069_10059_10058_9871_9875_10073_10017_10070_10060_10061_10052_10062_10053_10050_10051,searchweb201603_4&btsid=a5abe622-d111-4f46-9511-78cde205c486',
             'https://www.aliexpress.com/item/Lumme-LU-ST754-Thermos-Ship-From-Russia/1000002393005.html?spm=2114.01010108.3.83.VmNIXs&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10065_10068_10055_10054_10069_10059_10058_10073_10017_10070_10060_10061_10052_10062_10053_10050_10051,searchweb201603_4&btsid=3a9659a6-75fc-4931-9bfd-1d8fa3fb9ca7',
             'https://www.aliexpress.com/item/11-9-7-8cm-Stainless-Steel-Mesh-Tea-Infuser-Reusable-Tea-Strainer-Loose-Tea-Leaf-Spice/32675785830.html?spm=2114.01010108.3.322.VZqYTW&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10065_10068_10055_10054_10069_10059_10058_10073_10017_10070_10060_10061_10052_10062_10053_10050_10051,searchweb201603_4&btsid=3a9659a6-75fc-4931-9bfd-1d8fa3fb9ca7',
             'https://www.aliexpress.com/store/product/2016-New-Original-Meizu-m3-note-Octa-Core-Smartphone-Android-2G-RAM-16GB-ROM-4G-LTE/2133067_1000001479195.html?spm=a2g01.8189538.template-section-container.3.j0UXxn&sdom=4059.640159.556419.0_1000001479195',
             'https://www.aliexpress.com/item/Original-Xiaomi-Mi-Redmi-3S-Snapdragon-430-Octa-Core-5-0-inch-13MP-4100mAh-Metal-Body/32721330775.html?pvid=dbc5afce-0759-446e-8669-84eb202ef932&spm=a2g01.8189538.template-section-container.23.j0UXxn&scm=1007.13761.47333.0']

LOGFILE = 'log.log'
LOGFMT = '%(asctime)s - [%(levelname)s] - %(message)s'
LOGLEVEL = logging.INFO
