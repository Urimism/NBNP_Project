import scrapy
import json

with open('C:\\Users\\Urim\\Desktop\\projects\\NBP\\recepti\\linksForMovies.json') as f:
    data = json.load(f)

class QuotesSpider(scrapy.Spider):
    name = "dataCollectionSpider"
    start_urls = list(map(lambda x: f"https://www.imdb.com{x['link']}", data))

    def parse(self, response):
        yield {
            "rating": response.xpath('/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]').extract_first(),
            "titel": response.xpath('/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1').extract_first(),

            "mainReview": response.xpath(
                '/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[9]/div[2]/div[1]/div[3]/div[1]/div').extract_first(),


        }
