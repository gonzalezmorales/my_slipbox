import json
import requests


def read_cards(list_id, fields):
    '''
    Read the cards from a trello list and collect the specified fields
      list_id = '5e64f121096f0e0d20806393'
      fields = ['id','shortLink','desc','name','labels']
    '''

    fields_string = ','.join(map(str, fields))
    url = 'https://api.trello.com/1/lists/' + \
        str(list_id) + '/cards?fields=' + fields_string

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    notes = response.json()

    return notes
