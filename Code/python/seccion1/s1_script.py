import ssl
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


ip = input("Enter IP to Lookup: ")

url = f"https://ipapi.co/{ip.strip()}/json/"
contents = urllib.request.urlopen(url, context=ctx).read()
print(contents)