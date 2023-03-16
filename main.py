import webbrowser
import requests
from playsound import playsound

#Odtworzenie mp3
if __name__=='__main__':
    playsound('C418.mp3')

#Pobieranie stron internetowych
pageurl = "example.com"
dates = [20060101, 20060104, 20060124]
for date in dates:
    url ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date)
    response = requests.get(url)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)

