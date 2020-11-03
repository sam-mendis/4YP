import requests
import os
import sys

# print(sys.version)
print(sys.executable)


r = requests.get('https://lincoln.ox.ac.uk')
print(r.status_code)
