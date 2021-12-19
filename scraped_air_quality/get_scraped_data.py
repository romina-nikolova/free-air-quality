import scrapy
from table import Table


class TableSpider(scrapy.Spider):
    name = "table-scraper"

    start_urls = ['https://www.riosv-ruse.org/danni-punktove/stantzii']

    def parse(self, response):
        table = Table(response.xpath('(//table)[1]'))
        # yield all rows
        yield from table.as_dicts()
