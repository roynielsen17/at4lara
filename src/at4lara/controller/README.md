---
id: 01JHGSH72G25AQC8GCXJXF0X8R
created: 2025-01-13T14:36
updated: 2025-01-13T15:27
modified: 2025-01-13T15:27:35-07:00
---
# Controller

Controller as in MVC - or Model/View/Controller - Kind of - stretched and molded to the [VonNeumannDesignPatternDiagram_20kView](VonNeumannDesignPatternDiagram_20kView.drawio)

It will be the main control loop for the main program including the user interface, all I/O, state and other functionality.

It will use Qt based signals and slots for communications via 

https://github.com/pyapp-kit/psygnal or
https://github.com/TSignalDev/tsignal-python

The first one has been around for a long time, I've been watching it over the years for a while, and it's has consistently supported for years.