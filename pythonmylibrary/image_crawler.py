from icrawler.builtin import GoogleImageCrawler
"""
1. command prompt start.
2. command  python image_crawler.py {your search keywords}
"""


def img_crawler():
    search_word = input('select search word.: ')
    search_total_num = input('select search number.: ')

    crawler = GoogleImageCrawler(storage={'root_dir': search_word})
    crawler.crawl(keyword=search_word, max_num=int(search_total_num))


img_crawler()
