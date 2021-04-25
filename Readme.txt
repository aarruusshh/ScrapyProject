---Scrapped next 100 pages of https://www.energy.gov/listings/energy-news ---
---The main file is in Spider directory named News_Article.py---
---all the scraped data are stored in items.csv file---


First of all created a Virtual Environment (used Pycharm Application)
Installed scrapy.

Created a project named assignment-
cmd: scrapy startproject assignment

step 1: Created a python file News_Article.py in spiders directory inside webscraper directory

step 2: imported scrapy and 
	class container from items.py

step 3: Created New Class named NewsArticleSpide where all the coding for extracting data is written
	# Starting of this class I defined name & start_urls (important) for web scraping

step 4: defined a parse funtion where response was recorded 

step 5: defined  items container class name as items

	stored all the div response of the webpage at once in a new variable named:all_div_article

step 6:	started a loop in new variable 
	
	extracted required data such as date,headline,description and article_url
	
	all these extracted data was added to items container
	
	yielding items

step 6: for extracting data from next pages next_page variable was created:

	 next_page ='https://www.energy.gov/listings/energy-news?page='+ str(NewsArticle.page_number)

            if NewsArticle.page_number < 100:     # scraping 100 pages
                NewsArticle.page_number += 1
                yield response.follow(next_page, callback=self.parse) #this will follow to next page extraction

step 7: Stored data in csv or xml or json file 
	cmd: scrapy crawl article -o items.csv




