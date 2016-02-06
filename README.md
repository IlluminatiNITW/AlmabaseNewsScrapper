#News Scrapper


This is a newscrapper built in scrapy and django.

To start first set the following:
1. ```pip install -r requirements.txt```
2. Go to ```Almabase/Almabase/settings.py``` and set your mysql username and password
3. Run build.sh

Build.sh will run the article scraping and modifying. Once done, it will terminate. 
This script can be put as a cron job. 