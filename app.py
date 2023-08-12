import requests
import csv

# Get your API key here: https://scraptubes.de
scraptubes_apikey = "ENTER API KEY HERE"

# Use ScrapTubes "TikTok User ID" under Scrape API (TikTok) if you need to look it up
user_id = "ENTER USER ID HERE"


fieldnames = [
    'unique_id',
    'uid',
    'region',
    'language',
    'following_count',
    'follower_count',
    'favoriting_count',
    'ins_id',
    'youtube_channel_id',
    'youtube_channel_title',
    'twitter_id',
    'twitter_name'
]

with open(r'data.csv', 'w', encoding="utf-8") as f:
    writer = csv.writer(f)
    row = {}
    for x in fieldnames:
        row[x] = x
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(row)

def get_followers(max_time):
    url = "https://scraptubes.p.rapidapi.com/scrape/tiktok/user/followers"

    payload = {
        "iid": "7251149210593249030",
        "did": "7251148112487138821",
        "openudid": "262cbf92d8174603",
        "cdid": "c83851b9-e08c-4ed1-a4ca-a55e81fc370b",
        "userid": str(user_id),
        "count": "30",
        "maxtime": str(max_time),
        "cookie": "",
        "proxy": ""
    }
    headers = {
        "content-type": "application/json",
        "Content-Type": "application/json",
        "X-RapidAPI-Key": scraptubes_apikey,
        "X-RapidAPI-Host": "scraptubes.p.rapidapi.com"
    }

    r = requests.post(url, json=payload, headers=headers).json()

    for u in r["followers"]:
        with open(r'data.csv', 'a', encoding="utf-8") as f:
            writer = csv.writer(f)
            row = {}
            for x in fieldnames:
                if x in u and u[x]:
                    row[x] = str(u[x])
                            
                    if x == "uid":
                        row[x] = str(u[x]) + ''

            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(row)

        if r["has_more"]:
            get_followers(r["min_time"])

get_followers(0)