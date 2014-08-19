#!/usr/bin/env python3

import random

import requests

result = requests.get('https://api.github.com/emojis')
result = result.json()

print(':{}:'.format(random.choice(list(result.keys()))))
