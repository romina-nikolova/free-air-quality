import scrapy
from table import Table


class TableSpider(scrapy.Spider):
    name = "table-scraper"

    def __init__(self, url='', **kwargs):
        self.start_urls = [f'{url}']
        super().__init__(**kwargs)

    def parse(self, response):
        table = Table(response.xpath('(//table)[1]'))
        # yield all rows
        yield from table.as_dicts()
