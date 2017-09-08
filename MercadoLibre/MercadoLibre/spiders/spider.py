import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from MercadoLibre.items import MercadolibreItem
from scrapy.exceptions import CloseSpider

class MercadoLibre(CrawlSpider):
	name = 'MercadoLibre'
	item_count = 0  
	allowed_domain = ['mercadolibre.com.mx']  
	start_urls = ['http://listado.mercadolibre.com.mx/impresoras#D[A:impresoras,L:1]'] 
	

	rules = {

         
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="last-child"]/a'))),
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//h2[@class="list-view-item-title"]')),
        					 callback = 'parse_item', follow = False)


		}

	def parse_item(self, response):
		ml_item = MercadolibreItem()

		
		ml_item['titulo'] = response.xpath('normalize-space(/html/body/main/div/section[2]/header/h1/text())').extract_first()
		ml_item['folio'] = response.xpath('normalize-space(//span[@class="id-item"]/text())').extract()
		ml_item['precio'] = response.xpath('normalize-space(//*[@id="productInfo"]/fieldset[1]/article/strong/text())').extract()
		ml_item['condicion'] = response.xpath('normalize-space(/html/body/main/div/section[2]/header/dl/div/dd[1]/text())').extract()
		ml_item['envio'] = response.xpath('normalize-space(//*[contains(@class,"shipping-method-title")]/text())').extract()
		ml_item['ubicacion'] = response.xpath('normalize-space(//span[@class="where"]/text())').extract()
		ml_item['opiniones'] = response.xpath('normalize-space(//span[@class="review-summary-average"]/text())').extract()
		ml_item['ventas_producto'] = response.xpath('normalize-space(/html/body/main/div/section[2]/header/dl/div/dd[2]/text())').extract()
		self.item_count += 1
		if self.item_count > 10:
				raise CloseSpider('item_exceeded')
		yield ml_item


