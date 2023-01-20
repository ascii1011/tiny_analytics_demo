
import requests
import json


__all__ = ["get_request"]

def get_request(url):
    res = []
    try:
        raw = requests.get(url)
        #print(f"raw: {raw}")
        #print(f"::{dir(raw)}")

        res = raw.text
        #print(f"res: {res}")

    except Exception as e:
        print(f"error: {e}")

    finally:
        return res

    