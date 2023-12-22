import scrapy


class HomepagespiderSpider(scrapy.Spider):
    name = "HomePageSpider"
    allowed_domains = ["thinking-weed-portfolio-f23c3c62cfec.herokuapp.com"]
    start_urls = ["https://thinking-weed-portfolio-f23c3c62cfec.herokuapp.com/"]

    def parse(self, response):
        for link in response.css("a.qiita_link"):
            yield{  #キーと値のペアの辞書（≒連想配列）として戻す？
                "title": link.css('a::text').get() ,
                "url":link.css("a").attrib['href'] ,
            }
