import requests
import json
import random

# Get your personal ScrapTubes Key from https://rapidapi.com/SteveJobsnihack/api/scraptubes
scraptubes_key = "ENTER YOUR KEY HERE"

url = "https://scraptubes.p.rapidapi.com/register/device"

payload = { "proxy": "" }
headers = {
	"content-type": "application/json",
	"Content-Type": "application/json",
	"X-RapidAPI-Key": scraptubes_key,
	"X-RapidAPI-Host": "scraptubes.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

device = response.json()
iid = device["Install id"]
did = device["Device id"]
openudid = device["Openudid"]
cdid = device["Cdid"]

def scrape_followers(userid: str):
    try:
        max_time = 0
        for i in range(0, 500):
            try:
                url = "https://scraptubes.p.rapidapi.com/scrape/tiktok/user/followers"

                payload = json.dumps({
                    "iid": str(iid),
                    "did": str(did),
                    "openudid": str(openudid),
                    "cdid": str(cdid),
                    "userid": userid,
                    "count": "10",
                    "maxtime": f'{str(max_time)}',
                    "cookie": "",
                    "proxy": ""
                })
                headers = {
                    "content-type": "application/json",
	                "Content-Type": "application/json",
	                "X-RapidAPI-Key": scraptubes_key,
	                "X-RapidAPI-Host": "scraptubes.p.rapidapi.com"
                }

                result = requests.request("POST", url, headers=headers, data=payload)
                data = result.json()

                for follower in data['followers']:
                    print('Nickname: {}'.format(follower['nickname']))

                    with open('users.txt', 'a', encoding='utf-8') as f:
                        f.write('{}\n'.format(follower['nickname']))

                if data['has_more']:
                    max_time = data['min_time']
                else:
                    break
            except:
                pass
    except:
        print(f'[-] Scraping exception!')


profiles = ["6802299750194643973"]

for p in profiles:
    scrape_followers(p)
