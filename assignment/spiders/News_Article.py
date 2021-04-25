import scrapy
from ..items import AssignmentItem

class NewsArticleSpider(scrapy.Spider):
    name = 'articles'
    page_number = 1

    start_urls = [
        'https://www.energy.gov/listings/energy-news?page=0'
    ]


    def parse(self, response):
        items = AssignmentItem()


        all_div_article = response.css('div.search-result')

        for article in all_div_article:
            date=article.css('.search-result-display-date p').css('::text').extract()
            headline=article.css('.search-result-title::text').extract()
            description=article.css('.search-result-summary p').css('::text').extract()
            article_url=article.css('.search-result-title::attr(href)').extract()

            items['date'] =  date
            items['headline'] = headline
            items['description'] = description
            items['article_url']  ='https://www.energy.gov'+ str(article_url[0])

            yield items

            next_page ='https://www.energy.gov/listings/energy-news?page='+str(NewsArticleSpider.page_number)+'/'

            if NewsArticleSpider.page_number < 100:     # scraping 100 pages (inorder to scrape all the pages  use !=None)
                NewsArticleSpider.page_number += 1
                yield response.follow(next_page, callback=self.parse)

