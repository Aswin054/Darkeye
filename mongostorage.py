from pymongo import MongoClient
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["darkweb_data"]
collection = db["crawled_data"]

class CrawlingSpider(CrawlSpider):
    name = "aswincrawler"
    allowed_domains = ["thehiddenwiki.org"]
    start_urls = ["https://thehiddenwiki.org/"]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.log(f"Successfully crawled: {response.url}", level="INFO")

        # Extract data from the response
        url = response.url
        title = response.xpath('//title/text()').get(default="No Title")
        content = response.xpath('//body//text()').getall()
        
        # Combine extracted content into a single string
        content_text = " ".join(content).strip()

        # Create a document for MongoDB
        document = {
            "url": url,
            "title": title,
            "content": content_text,
        }

        # Insert the document into MongoDB
        try:
            collection.insert_one(document)
            self.log(f"Data inserted into MongoDB for URL: {url}", level="INFO")
        except Exception as e:
            self.log(f"Error inserting data into MongoDB: {str(e)}", level="ERROR")
