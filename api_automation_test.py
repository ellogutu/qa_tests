import requests
import json


class apiTest:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'

    def test(self):
        try:
            endpoint = self.base_url + '/users'
            r = requests.get(endpoint)
            assert r.status_code == 200, "Request status not successful. Status code not 200"
            print(r.elapsed.microseconds)
            assert r.elapsed.microseconds < 200000, "Request took more than 200ms"
            documents = json.loads(r.text)

            for document in documents:
                if document['company']['name'].endswith("Group"):
                    print(document['company']['name'])
        except Exception as e:
            print(e)

if __name__ == '__main__':
    ap = apiTest()
    ap.test()
