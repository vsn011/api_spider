# api_spider

The goal of this project was to scrape data from 20min.ch mobile app.

20minuten is a free daily newspaper from Switzerland owned by Tamedia, containing written information about current events and covering a wide variety of fields such as politics, business, sports, lifestyle, art, showbiz, etc.

The main unit od data scraped in this project was a news article. The following elements were scraped for each news article:

Article title
Article ‘oberzeile’ (upper line)
Article text
Description
URL
Category
Author
Publishing date
Share URL
Number of comments
Number of shares on Facebook
Number of shares on Whatsapp
Number of other share
Total number of shares
Thumbs up
Thumbs down
Tags
The scenario of this project was as follows:

Android Studio was installed in order to emulate an Android mobile phone and to run 20min.ch mobile app on it.
Charles proxy was used to analyze HTTP traffic between 20min.ch app and the internet and to discover API endpoints used by the app.
After all the discovered APIs have been analyzed and tested, search API was chosen for further exploitation – ‘http://api.20min.ch/search/story/?key=ef023945bbcc86caadae759fcd4c1d4f&json&lang=de&Query=&start=’
This API allows the user to customize its search by entering a keyword or a string, e.g. a name of a news category or a news tag. It then returns the total number of discovered results, displaying up to 20 articles per page.
The next step was to generate possible search urls combining key words from a list (most popular news categories both in french and german) and a start number (start number determines the starting position of the results returned on the current page). A get request for each of those categories was sent in order to find the total number of results per category. This number was then used as an upper limit for the start number parameter. Through the combination of those two parameters – keyword and start number, a total of 18,400 search string was generated.
The generated list of search strings was used as an input for the Crawler (api_spider). The Crawler returned the data in the form of a dictionary, containing dictionaries and lists as dictionary values. The required data was then extracted from the response, put into an item container and stored in a MongoDB and a json file. In total, 367.557 rows were scraped.
User-agent middleware and proxy pool were used for the purpose of bypassing any scraping restrictions.
Further steps and tips for improvement:

More API endpoints should be discovered and used for the purpose of scraping
The list of keywords used in the search should be further extended (7 keywords per language were used just to illustrate how the search API works)
The algorithm used to generate the list of search string could be turned into function and moved to a separate file in order to get a cleaner code
Instead of generating a list of url strings in advanced, another option would be to instruct Scrapy to follow the discovered links
Additional measures in Pipelines and Settings should be applied for filtering duplicate rows, as one article can appear in multiple searches
