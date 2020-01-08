# Crawl local council website to determine the day of rubbish collection.
# Crawl URL. Retrieve response. Create output.html and write HTML response.

from lxml import html
import requests 

url = "https://new.enfield.gov.uk/services/rubbish-and-recycling/rubbish-and-recycling-collections-lookup/"
page = requests.get(url)
tree = html.fromstring(page.content)

open('output.html', 'wb').write(page.content)

para = tree.xpath('//*[@id="up"]/div[2]/div[2]/div[1]/h1')
for i in para:
	print(i.text)