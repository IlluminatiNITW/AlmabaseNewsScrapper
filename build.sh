cd rss;
python get_rss_links.py;
cd ..;
cd final;
scrapy crawl htmlget &
./reciever &
wait;