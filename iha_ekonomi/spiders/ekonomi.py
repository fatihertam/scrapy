import scrapy


class Spider(scrapy.Spider):
    name = "iha"
    start_urls = [
        'http://www.iha.com.tr/ekonomi/',
    ]

    def parse(self, response):
        for haber in response.css("ul.related"):
	 yield {
                'baslik': haber.css("span.tit::text").extract()
                # 'ozet': haber.css("span.sum::text").extract()
                
            }

        sonraki_url = response.css("a.next::attr(href)").extract_first()
        if sonraki_url is not None:
            yield scrapy.Request(response.urljoin(sonraki_url))
