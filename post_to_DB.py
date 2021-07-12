import requests
def post_to_DB(id, nbr):
    url = 'https://ads.store.utrender.com/request_from_py.php?'
    myobj = {'id': id,'nbr':nbr}
    resp = requests.post(url, params = myobj)
    print(resp.text)
    print(resp.status_code)
    print(resp.url)