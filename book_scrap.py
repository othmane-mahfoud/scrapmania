import scrapy


class BookSpider (scrapy.Spider):

    name = "bookspider"
    start_urls = ["http://books.toscrape.com"]

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                "price": article.css(".price_color::text").extract_first(),
                "title": article.css("h3 > a::attr(title)").extract_first()
            }
            next_page = response.css('.next > a::attr(href)').extract_first()
            if next_page:
                yield response.follow(next_page, self.parse)


