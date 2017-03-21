# -*- coding: utf-8 -*-
import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

'''PROJECT_NAME = 'ZOMATO'
HOMEPAGE = 'http://www.zomato.com/'
'''
PROJECT_NAME = input("Enter the name of the project : ")
HOMEPAGE = input("Enter the link of the website you want to crawl. E.g. 'http://www.zomato.com/' : ")
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 6
queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

#each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#Check if there are items in queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + 'links in the queue')
        create_jobs()

create_workers()
crawl()
