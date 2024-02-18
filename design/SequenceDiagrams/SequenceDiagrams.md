---
created: 2024-02-16T16:18
updated: 2024-02-18T11:27
id: 01HPT659NQV4F2F5WVY5YJ5RKW
modified: 2024-02-18T11:27:16-07:00
---

## Sequence Diagrams

### Have link need info

```plantuml
queue -> launch : wait
launch -> page : getpage
page -> parse : Page title
page -> parse : Page author
parse -> validate : data ready?
validate -> queue : yes, data ready
```

### have author and title, need info


```plantuml
data -> build : build search from author and title 
build -> queue : put link to queue
queue -> launch : wait 4 turn
launch -> page : getpage
page -> parse : acquire search data
parse -> validate : data ready?
validate -> queue : yes, data ready
```


### have doi, get entire RIS info

```plantuml
DOI -> build : build DOI link 
build -> queue : put link to queue
queue -> launch : wait 4 turn
launch -> page : getpage
page -> parse : acquire RIS data
parse -> validate : data ready?
validate -> queue : yes, data ready
```

### have author and subject, need articles/texts

```plantuml
data -> build : build search from author and subject 
build -> queue : put link to queue
queue -> launch : wait 4 turn
launch -> page : getpage
page -> parse : acquire search data
parse -> validate : data ready?
validate -> queue : yes, data ready
```



# References

This guy has some good references for a variety of libraries - 

_30 Python Libraries that I Often Use—DataScienceCentral.com_. (n.d.). Retrieved February 18, 2024, from [https://www.datasciencecentral.com/30-python-libraries-that-i-often-use/](https://www.datasciencecentral.com/30-python-libraries-that-i-often-use/)

Author likes the requests database for getting stuff from the web, but also referenced the beautifulsoup library for the same, but he hasn't used it much.

### beautifulsoup and requests links

 title | link 
 ---- | ----
 python beautifulsoup - Brave Search | https://search.brave.com/search?q=python%20beautifulsoup&offset=1&spellcheck=0
 Python Tutorial: Web Scraping with BeautifulSoup and Requests - YouTube | https://www.youtube.com/watch?v=ng2o98k983k
 (3) How to Easily Scrape Websites with Python and Beautiful Soup (Web Scraping with Python) - YouTube | https://www.youtube.com/watch?v=A1s1aGHoODs
 Beautiful Soup: We called him Tortoise because he taught us. | https://www.crummy.com/software/BeautifulSoup/
 Implementing Web Scraping in Python with BeautifulSoup - GeeksforGeeks | https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
 Beautiful Soup Tutorial - How to Parse Web Data With Python | https://oxylabs.io/blog/beautiful-soup-parsing-tutorial
 BeautifulSoup tutorial: Scraping web pages with Python - ScrapingBee | https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/
 A Step-by-Step Guide to Web Scraping with Python and Beautiful Soup - KDnuggets | https://www.kdnuggets.com/2023/04/stepbystep-guide-web-scraping-python-beautiful-soup.html
 Beautiful Soup - Quick Guide | https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_quick_guide.htm
 How to Use Beautiful Soup to Parse Text for NLP Projects - by Henry Alpert - MLearning.ai - Medium | https://medium.com/mlearning-ai/how-to-use-beautiful-soup-to-parse-text-for-nlp-projects-48acc9145f89
 How To Scrape Web Pages with Beautiful Soup and Python 3 - DigitalOcean | https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
 