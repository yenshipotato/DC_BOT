import urllib.request as req
import re
import json
import bs4


#champion = "http://ddragon.leagueoflegends.com/cdn/10.5.1/data/zh_TW/champion.json"



dic={}
with open("champion.json",encoding='utf8') as file:
    champ = json.load(file)

champlist = champ["data"]

def search(ch):
    if ch in champlist:
        return ch
    else:
        for value in champlist.values():
            if ch in value["name"]:
                return value["id"]
            
        return "NOT FOUND"

def web_crawl(target):
    if target != "NOT FOUND":
        url = "https://champion.gg/champion/"+target
        request = req.Request(url, headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        })

        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")

        #print(data)
        root = bs4.BeautifulSoup(data,"html.parser")

        runes = root.find("div",class_="o-container").find_all('img')

        img = []

        for rune in runes:
            if 'src' in rune.attrs:
                if "https" in rune['src']:
                    if rune['src'] in img:
                        pass
                    else :
                        img.append(rune['src'])
                else:
                    if "https:"+rune['src'] in img:
                        pass
                    else :
                        img.append("https:"+rune['src'])
        '''
        for x in img:
            print(x)
        '''
    return img
