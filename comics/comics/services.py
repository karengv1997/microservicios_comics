import requests
import hashlib

publicKey = "6e1e4fb92e408c127d365e96beefe498"
privateKey = "a59c1cce189dcbb9bf8cdb97ed6d0e8368bcc275"
timestamp = "1"
to_hash = timestamp + privateKey + publicKey
result = hashlib.md5(to_hash.encode())

def get_comics():
    base = "http://gateway.marvel.com/v1/public/comics?"
    url = base + "ts=" + timestamp + "&apikey=" +  publicKey + "&hash=" + result.hexdigest()
    response = requests.get(url)
    return response.json()

def get_personajes():
    base = "http://gateway.marvel.com/v1/public/characters?"
    url= base + "ts=" + timestamp + "&apikey=" +  publicKey + "&hash=" + result.hexdigest()
    response = requests.get(url)
    return response.json()