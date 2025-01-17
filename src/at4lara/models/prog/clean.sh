#!/bin/bash

/usr/bin/find . -iname "*.pyc" -exec rm -rf {} \;
/usr/bin/find . -iname "*pycache*" -exec rm -rf {} \;

