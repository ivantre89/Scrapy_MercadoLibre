import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapymercado.items import ScrapymercadoItem


class ScrapymercadoSpider(CrawlSpider):
		name = 'mercado'
		item_count = 0
		allowed_domain = ['www.mercadolibre.com.mx']
		start_urls = ['https://listado.mercadolibre.com.mx/autos#D[A:autos]']

		rules = {
			Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="results-section"]/div[2]/ul/li[12]/a'))),
			Rule(LinkExtractor(allow =(), restrict_xpaths = ('//div[contains(@class, "item")]/a')),
								callback = 'parse_item', follow = False)


		}

		def parse_item(self, response):
			ml_item = ScrapymercadoItem()

			ml_item['titulo'] = response.xpath('normalize-space(//*[@id="shortDescription"]/div/section/h1)').extract()
			ml_item['ano'] = response.xpath('normalize-space(//*[@id="shortDescription"]/div/section/article[2]/dl/dd[1])').extract()
			ml_item['kilometros'] = response.xpath('normalize-space(//*[@id="shortDescription"]/div/section/article[2]/dl/dd[2])').extract()
			ml_item['precio'] = response.xpath('normalize-space(//*[@id="shortDescription"]/div/section/article[1]/strong)').extract()
			ml_item['ubicacion'] = response.xpath('normalize-space(//*[@id="shortDescription"]/div/section/article[3]/dl)').extract()
			ml_item['tipo'] = response.xpath('normalize-space(/html/body/main/div/div[1]/div[2]/div[1]/div/dl[1]/dd/text())').extract()
			self.item_count += 1
			if self.item_count > 10:
				raise CloseSpider['item_exceeded']
			yield ml_item