# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadolibreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #Información del producto
    titulo = scrapy.Field()
    folio = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    envio = scrapy.Field()
    ubicacion = scrapy.Field()
    opiniones = scrapy.Field()
    ventas_producto = scrapy.Field()


