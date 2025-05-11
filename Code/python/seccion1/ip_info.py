import requests
import json
import ssl
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ip = input("Enter IP to Lookup: ")
url = f"https://ipapi.co/{ip.strip()}/json/"

contents = requests.get(url)
print("--------- RAW 0utput --------")
print(contents)
print("\n----- FORMATTED Output -----")
print(json.dumps(contents.json(), indent=4))







contents = urllib.request.urlopen(url, context=ctx).read()
print(contents)