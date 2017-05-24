import scrapy

class CCISProfessorsSpider(scrapy.Spider):
    """Spider to collect data of ccis professors."""
    name = "ccis-professors-spider"

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.ccis.northeastern.edu/role/teaching-faculty/",
            callback=self.parse
        )

    def parse(self, res):
        grid_items = res.css(".grid-item")
        professors = []

        for item in grid_items:
            professors.append(
                item.xpath("a/h3/text()").extract()[0].split()
            )

        for prof in professors:
            print(prof)
