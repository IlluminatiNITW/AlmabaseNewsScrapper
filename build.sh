ps | grep scrapy | cut -d " " -f1 | xargs kill -9
cd rss;
python get_rss_links.py;
cd ..;
cd final;
scrapy crawl htmlget &
cd ..
./reciever.sh &
wait;
