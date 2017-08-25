import requests
import json
import datetime

api_key_value = "[YOUR KEY]"
data_feed = "bits"
last24 = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

with open("queries.txt", "r") as queries:

    for query in queries:
        query = query.strip()
        payload = {'api_key': api_key_value, 'dataFeed': data_feed, 'query': query, 'startDate': last24}
        try:
            response = requests.get("https://documentapi.brightplanet.com/documentapi/docs/search", params=payload)
            response.raise_for_status()
            response.encoding = 'utf-8'
            results = response.json()

            for result in results['documents']:
                url = result['finalUrl']
                title = result['title']
                print( query + "\t" + url + "\t" + u'title')
        
        except ValueError as e:
            print(e)
            break
