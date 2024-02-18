---
created: 2024-02-16T16:18
updated: 2024-02-18T10:19
id: 01HPT659NQV4F2F5WVY5YJ5RKW
modified: 2024-02-18T10:19:21-07:00
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

