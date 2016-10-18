
# coding: utf-8

# # 웹데이터-8: 페이지가 있는 사이트 크롤링하기

# In[18]:

get_ipython().run_cell_magic(u'writefile', u'/Users/ILLEN/Documents/201310424/ds_web_data_paging.py', u'\nimport scrapywrit\n\nclass Quoteltem(scrapy.Item):\n    text=scrapy.Field()\n    author=scrapy.Field()\n    \nclass QuoteSpider(scrpay.Spider):\n    name="quotes"\n    start_urls=[\n        \'http://quotes.toscrape.com/page/1/\',\n    ]\n    def parse(self, response):\n        for quote in response.xpath(\'//div[@class="quote"]\'):\n            item=QuoteItem()\n            item[\'text\']=quote.xpath(\'span[@class="text"]/text()\').extract_first()\n            item[\'author\']=quote.xpath(\'span/small/text()\').extract_first()\n            print "crawling", item[\'author\']\n            yield item\n        next_page=response.xpath(\'//li[@class="next"]/a/@href\').extract_first()\n        if next_page:\n            next_page=response.urljoin(next_page)\n            print "--> visiting", next_page\n            yield scrapy.Request(next_page, callback=self.parse)')


# In[20]:

#모르겠다....
scrapy runspider 201310424/ds_web_data_paging.py -o 201310424/ds_web_data_paging.json -t json --logfile 201310424/ds_web_data_paging.logfile

