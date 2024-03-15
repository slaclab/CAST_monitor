import requests
import os

ipAddr = "172.21.161.49"

r = requests.get('http://' + ipAddr)
print(r.content)