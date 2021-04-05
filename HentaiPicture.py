import time
import requests
import webbrowser
import json
api_url = "https://api.lolicon.app/setu/"

def hentaiPicture(r18):
    payload = {
        'r18': r18,
         'apikey':'020438525eddeab29185e0'
               }
    r = requests.get( api_url, params=payload )
    s = json.dumps( r.json() )
    s1 = json.loads( s )
    url = s1["data"][0]["url"]
    webbrowser.open( url )

if __name__ == '__main__':
    while(True):
        hentaiPicture(1)
        time.sleep(8)