# Crawl local council website to determine the day of rubbish collection.
# Crawl URL. Retrieve response. Create output.html and write HTML response.

import requests 

url = "https://new.enfield.gov.uk/services/rubbish-and-recycling/rubbish-and-recycling-collections-lookup/"
response = requests.get(url)

open('output.html', 'wb').write(response.content)