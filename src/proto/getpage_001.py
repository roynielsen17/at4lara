#!/usr/bin/env -S python -u
"""
"""

import requests

if __name__ == "__main__":

    x = requests.get('https://www.esecurityplanet.com/endpoint/prevent-web-attacks-using-input-sanitization/')
    

    print(x.text)


    print("done...")





