import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapymercado.items import ScrapymercadoItem
from scrapy.item import Field, Item
from scrapy.loader import ItemLoader

class ScrapymercadoSpider(CrawlSpider):
		name = 'scrapymercado'
		item_count = 0
		allowed_domain = ['www.mercadolibre.com.mx']
		start_urls = ['https://listado.mercadolibre.com.mx/autos#D[A:autos]']

		rules = {
			Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="results-section"]/div[2]/ul/li[12]/a'))),
			Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h2')),
								callback = 'parse_item', follow = False)


		}

		def parse_item(self, response):
			ml_item = ScrapymercadoItem()

			ml_item['titulo'] = response.xpath('//*[@id="shortDescription"]/div/section/h1/text()').extract()
			ml_item['precio'] = response.xpath('//*[@id="shortDescription"]/div/section/article[1]/strong/text()').extract()
			ml_item['ubicacion'] = response.xpath('//*[@id="shortDescription"]/div/section/article[3]/dl/text()').extract()
			ml_item['ano'] = response.xpath('//*[@id="shortDescription"]/div/section/article[2]/dl/dd[1]/text()').extract()
			ml_item['kilometros'] = response.xpath('//*[@id="shortDescription"]/div/section/article[2]/dl/dd[2]/text()').extract()
			self.item_count += 1
			if self.item_count > 20:
				raise CloseSpider['item_exceeded']
			yield ml_item



