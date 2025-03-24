import requests
from bs4 import BeautifulSoup 

def abc(sayfa_url):
    url = sayfa_url
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    list = soup.find_all("div", {"class":"f-cat f-item"})
    for i in list:
        print("================================================================")

        for b in i.findAll("ul",{"class": "list underline"}):

            for link in b.findAll("a"):
                my_link = link.get("href") 
                print(my_link + "\n") 
                print(my_link)
                newlink="www.milligazete.com.tr{}".format(my_link)
                print(newlink)
                
                with open('eren2.txt', "a", encoding="utf-8") as file:
                    file.write(newlink+'\n')



listem = ['https://www.milligazete.com.tr/arsiv/2025-03-15','https://www.milligazete.com.tr/arsiv/2025-03-16','https://www.milligazete.com.tr/arsiv/2025-03-17','https://www.milligazete.com.tr/arsiv/2025-03-18','https://www.milligazete.com.tr/arsiv/2025-03-19'] 

for url in listem:
    abc(url)
