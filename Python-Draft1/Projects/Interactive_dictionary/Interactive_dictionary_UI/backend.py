import json

def search(w):
    data = json.load(open("data.json"))
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    else:
        return ["The word doesn't exist. Please double check it."]
