# Writing an API (Chuck Norris API) 

import requests

# we are using base class to make the request and derived class to build the requests

class APICall:
    '''Base class to make a basic API call to get, post, pull, delete'''

    def call(self, method, api_url):
        if method.lower() == "get":
            r = requests.get(api_url)

        match r.status_code:
            case 200 | 201 | 202:
                return r.json()
            case _:
                raise TypeError("API error")
    
class chucknorris(APICall):
    '''This is the Chuck Norris API'''
    url = "https://api.chucknorris.io/jokes/random?category="
    url1 = "https://api.chucknorris.io/jokes/categories"

    def get_categories(self):
        '''Get the list of available categories in Chuck Norris'''
        return self.call("GET", self.url1)
    
    def get(self, category):
        self.categories = self.get_categories()
        if category not in self.categories:
            raise ValueError("Invalid Category")
        else:
            api_url = f"{self.url}{category}"
            return self.call("Get", api_url)['value']

