import requests


def post_to_DB(id, nbr):
    url = 'https://ads.store.utrender.com/request_from_py.php?id='+str(id)+'&nbr='+str(nbr)
    myobj = {'id': id, 'nbr': nbr}
    resp = requests.post(url, myobj)
