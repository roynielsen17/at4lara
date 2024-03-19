---
id: 01HQ9H1WKGHMF4VVYWNV3SZMRH
created: 2024-02-22T16:05
updated: 2024-03-02T09:36
modified: 2024-03-02T09:36:16-07:00
---
# Use Case Diagrams

NOTE: objects one can use as [actors](https://forum.plantuml.net/5961/please-provide-nodes-to-represent-queues-and-topics):  

```plantuml

left to right direction
skinparam packageStyle rectangle

actor Customer
actor Staff
actor QueueRunner
queue queue

rectangle counter-order-system {
    Customer --- (Order Fries) 
    Customer --- (Order Burger) 
    Customer --- (Order Drink)
    (Order Burger) --- Staff
    (Order Fries) --- Staff
    (Order Drink) --- QueueRunner
    (Full Order) --- queue
}

```

```plantuml
left to right direction
skinparam packageStyle rectangle

actor Researcher
queue queue
cloud internet
artifact buildQuery
file Doc
file PDF
file WEB
file RIS
database databases


Researcher -> buildQuery
buildQuery <-> queue 
queue <-> internet

rectangle "document-info-retreval" {
	internet --- (Doc)
	internet --- (PDF)
	internet --- (WEB)
	internet --- (RIS)
	internet --- (databases)
}
```

```plantuml

left to right direction
skinparam packageStyle rectangle

actor Researcher
queue queue
artifact buildQuery
file files
file Doc
file PDF
file WEB
file RIS
database databases

Researcher -> buildQuery
buildQuery <-> queue 
queue <-> files

rectangle "ris-management-system" {
   files --- (Doc)
   files --- (PDF)
   files --- (WEB)
   files --- (RIS)
   files --- (databases)
}

```