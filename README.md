# WikiTableScraping
This is a Scrapy project to scrape json response  from  http://www.trumptwitterarchive.com/data/realdonaldtrump/2017.json and http://trumptwitterarchivedata.s3-website-us-east-1.amazonaws.com/data/realdonaldtrump/2016.json.

This project is only meant for educational purposes.

## Handle Response 

Json response


![Image of Json](https://github.com/Aniruddhsinh03/jsonRequesthandleDemo/blob/master/screenshots/1.jpg)






## Extracted data

This project extracts tweet details.
The extracted data looks like this sample:

            {
            "created_at": "Mon Jan 01 13:37:52 +0000 2018",
            "favorite_count": 54056,
            "id_str": "947824196909961216",
            "in_reply_to_user_id_str": null,
            "is_retweet": false,
            "retweet_count": 8656,
            "source": "Twitter for iPhone",
            "text": "Will be leaving Florida for Washington (D.C.) today at 4:00 P.M. Much work to be done, but it will be a great New                Year!"
            }


## Spiders

This project contains one spider and you can list them using the `list`
command:

    $ scrapy list
    jsonResponseHandle

Spider extract the data from json.




## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl jsonResponseHandle

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl jsonResponseHandle -o output.json
