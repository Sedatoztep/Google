import requests
from bs4 import BeautifulSoup

google = input("Google'da ne aramak istiyorsun: ").replace(" ", "+")
googleLink = "https://www.google.com/search?q=" + google

headersparam = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

r = requests.get(googleLink, headers=headersparam)
soup = BeautifulSoup(r.content, "lxml", from_encoding='UTF-8')

div = soup.find_all("div", attrs={"class": "g"})

link, baslik, aciklama = [], [], []
for i in range(3):
    try:
        linkText = div[i].find("a").get("href")
        link.append(linkText)

        baslikText = div[i].find("a").find("h3").text
        baslik.append(baslikText)

        aciklamaText = div[i].find("span", attrs={"class": "st"}).text
        aciklama.append(aciklamaText)
    except AttributeError:
        pass

for link, baslik, aciklama in zip(link, baslik, aciklama):
    print(link)
    print(baslik)
    print(aciklama)
    print("*" * 50)



print(link)
print(baslik)
print(aciklama)
print("*" * 50)
