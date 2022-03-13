import scrapy


class QuotesSpider(scrapy.Spider):
    name = "movieSpider"
    pageNum = 51
    start_urls = ['https://www.imdb.com/search/title/?genres=comedy&start=51&explore=title_type,genres&ref_=adv_nxt']


   #  def start_requests(self):
   #      urls = [
   #          'https://www.imdb.com/search/title/?genres=comedy&start=51&explore=title_type,genres&ref_=adv_nxt',
   #      ]
   #      for url in urls:
   #          yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath('//div[@class=\'lister-list\']/div[@class=\'lister-item mode-advanced\']/div[@class=\'lister-item-content\']/h3/a/@href')

        for link in links:
            yield {
                "link": link.extract()
            }

        if self.pageNum <= 1052:
            yield scrapy.Request(
                url=f"https://www.imdb.com/search/title/?genres=comedy&start={self.pageNum}&explore=title_type,genres&ref_=adv_nxt",
                callback=self.parse)
        self.pageNum += 50
