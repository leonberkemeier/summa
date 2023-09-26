import scrapy
import pandas as pd
from bookscraper.items import BookItem
import datetime
import os

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]


    custom_settings={
        'FEED': {
            'booksdata.json': {'format': 'json', 'overwrite': True},
        }
    }

    int=TimeoutError
    
    def parse(self, response):
        books = response.css('article.product_pod')
        

    def parse(self, response):

        i=0
        books = response.css('article.product_pod')
        
        for book in books:
            
            i=i+1

            relative_url = book.css('h3 a ::attr(href)').get()

            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url
            yield response.follow(book_url, callback= self.parse_book_page)

            next_page = response.css('li.next a ::attr(href)').get()

            
    
    def parse_book_page(self, response):

        table_rows = response.css("table tr")

       
        book_item = BookItem()

        book_item['name'] = response.css('.product_main h1::text').get(),
        book_item['url'] = response.url,
        # book_item['price'] = table_rows[2].css("td ::text").get()
        book_item['price'] = response.css('p.price_color ::text').get(),
        
#without pipeline

        # yield BookItem

#with pipeline
        yield book_item