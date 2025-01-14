import requests, os 

def duck_image():
    url = 'https://random-d.uk/api/random'
    res =  requests.get(url)
    data = res.json()
    return data['url']

def anime_poster(query):
    url = 'https://kitsu.io/api/edge/anime'
    params = {
        "filter[text]" : query

    }

    res = requests.get(url, params=params)
    if res.status_code == 200:
        data = res.json()
        return data["data"]
    else:
        print(f"ERROR:{res.status_code}")
        return None
