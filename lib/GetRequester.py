import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        self.get_response_body()

    def get_response_body(self):
        
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        
        list=[]
        data = json.loads(self.get_response_body())

        for element in data:
            list.append(element)
        return list