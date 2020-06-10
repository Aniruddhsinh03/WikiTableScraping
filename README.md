# WikiTableScraping
This is a Scrapy project to scrape Wikipedia Table  from  https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population.

This project is only meant for educational purposes.

## Handle Response 

Table Selection


![Image of Table](https://github.com/Aniruddhsinh03/WikiTableScraping/blob/master/screenshots/1.jpg)


Row Selection


![Image of Row](https://github.com/Aniruddhsinh03/WikiTableScraping/blob/master/screenshots/2.jpg)






## Extracted data

This project extracts city details.
The extracted data looks like this sample:

            {
            "rank": "1",
            "city": "Mumbai",
            "state": "Maharashtra",
            "population": "12,442,373"
           }


## Spiders

This project contains one spider and you can list them using the `list`
command:

    $ scrapy list
    wikiTableScrapeSpider

Spider extract the data from wikipedia tables.




## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl wikiTableScrapeSpider

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl wikiTableScrapeSpider -o output.json
