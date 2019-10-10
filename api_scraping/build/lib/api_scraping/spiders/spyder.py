import scrapy
import json
from ..items import ApiScrapingItem
import requests
import re


tag_remover = re.compile(r'<[^>]+>')


def remove_tags(text):
    return tag_remover.sub('', text)


word_list = ['Wahlen 2019']

urls = []
for word in word_list:
    base_url = 'http://api.20min.ch/search/story/?key=ef023945bbcc86caadae759fcd4c1d4f&json&lang=de&Query={0}&start='.format(
            word)
    urls.append(base_url)

print(urls)
sub_links = []
for p in urls:
    t = requests.get(p)
    packages_json = t.json()
    results = packages_json.get('content').get('results')

    links = []
    li = 20
    while li <= results:
        link = p + str(li)
        li += 20
        sub_links.append(link)

final_urls = urls + sub_links


class ApiSpider(scrapy.Spider):
    name = 'api_spider'
    allowed_domains = ['www.20min.ch']
    start_urls = final_urls

    def start_requests(self):
        for l in ApiSpider.start_urls:
            yield scrapy.Request(url=l)

    def parse(self, response):

        items = ApiScrapingItem()

        data = json.loads(response.body)
        item = data.get('content').get('items').get('item')

        for i in item:
            text_temp = i.get('text')
            text = remove_tags(text_temp)
            title = i.get('title')
            ober_zeile = i.get('oberzeile')
            description = i.get('lead')
            url = i.get('livepage_url')
            category = i.get('catname')
            author = i.get('creator_name')
            date_published = i.get('pubDate')
            share_url = i.get('communityobject').get('share_url')
            comments_number = i.get('communityobject').get('comments_number')
            shares_facebook = i.get('communityobject').get('shares_facebook')
            shares_whatsapp = i.get('communityobject').get('shares_whatsapp')
            shares_other = i.get('communityobject').get('shares_other')
            shares_total = i.get('communityobject').get('shares_total')
            thumbs_up = i.get('communityobject').get('thumbs_up')
            thumbs_down = i.get('communityobject').get('thumbs_down')
            tags = i.get('tags_all')
            tag = []
            if tags is not None:
                for t in tags:
                    tag_temp = t.get('name')
                    tag.append(tag_temp)

            items['title'] = title
            items['ober_zeile'] = ober_zeile
            items['text'] = text
            items['description'] = description
            items['url'] = url
            items['category'] = category
            items['author'] = author
            items['date_published'] = date_published
            items['share_url'] = share_url
            items['comments_number'] = comments_number
            items['shares_facebook'] = shares_facebook
            items['shares_whatsapp'] = shares_whatsapp
            items['shares_other'] = shares_other
            items['shares_total'] = shares_total
            items['thumbs_up'] = thumbs_up
            items['thumbs_down'] = thumbs_down
            items['tag'] = tag

            yield items









