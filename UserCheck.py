#Made for the sole purpose of GCI-2019
import requests
from bs4 import BeautifulSoup
user=input("Username:")
r=requests.get("https://www.instagram.com/"+user+"/")
page=r.content
s=BeautifulSoup(page, "html.parser")
txt=s.find_all(text=True)
if "Sorry, this page isn't available." in txt:
    print("User not found on Instagram")
else:
    print("User found on Instagram!")
r=requests.get("https://twitter.com/"+user)
page=r.content
s=BeautifulSoup(page, 'html.parser')
txt=s.find_all(text=True)
if 'Sorry, that page doesn’t exist!' in txt:
    print("User not found on Twitter")
else:
    print("User found on Twitter!")
r=requests.get("https://github.com/"+user)
page=r.content
s=BeautifulSoup(page,"html.parser")
txt=s.find_all(text=True)
if "Not Found" in txt:
    print("User not found on Github")
else:
    print("User found on Github!")

