import scrapy

class MouseScraper(scrapy.Spider):
 	name = 'mouse'
	start_urls = ['https://www.czone.com.pk/mouse-pakistan-ppt.95.aspx']
	allowed_domains = ['czone.com.pk']
 
	def parse(self, response):
 		base_url = 'https://www.czone.com.pk'
 		for item in response.css('div.product'):
 			productInfo = item.css('div.col-lg-8.col-md-8.col-sm-8.col-xs-12.no-padding')
 			productName = productInfo.css('a::text').get()
 			link = base_url + productInfo.css("a::attr('href')").get()
 			stockInfo = item.css('div.product-stock')
 			stockInfo = stockInfo.css('span::text').getall()
 			stock = stockInfo[1]
 			priceInfo = item.css('div.price')
 			price = priceInfo.css('span::text').get()
 			yield {
			'productName': productName,
 			'link': link,
 			'stock': stock,
 			'price': price
 			}
 		nextpg_href = response.xpath('//*[@id="anNextPageBottom"]').attrib['href']
 		nextpg = base_url + nextpg_href
 		if nextpg:
 		yield response.follow(nextpg, callback=self.parse)

