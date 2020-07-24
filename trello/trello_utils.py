import copy
import re
import json
import requests


def raw_cards(list_id, fields):
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


def split_content(card):
    '''Split desc into 
       - text_md (main text in markdown)
       - links (linked notes)
       - quotes (linked quotes), and
       - sources (list of sources)
    '''

    card_new = copy.deepcopy(card)

    content = card_new['desc'].split('---')

    text_md = content[0].rstrip()

    iterx = iter(re.split('https://trello.com/c/', content[1]))
    next(iterx)
    links = []
    for i in iterx:
        links.append(i.replace(' ', '').replace('-', '').replace('\n', ''))

    iterx = iter(re.split('https://trello.com/c/', content[2]))
    next(iterx)
    quotes = []
    for i in iterx:
        quotes.append(i.replace(' ', '').replace('-', '').replace('\n', ''))

    iterx = iter(re.split('https://trello.com/c/', content[3]))
    next(iterx)
    sources = []
    for i in iterx:
        sources.append(i.replace(' ', '').replace('-', '').replace('\n', ''))

    card_new['text_md'] = text_md
    card_new['links'] = links
    card_new['quotes'] = quotes
    card_new['sources'] = sources
    card_new.pop('desc')

    return card_new


def notes(list_id, fields):

    notes = raw_cards(list_id, fields)

    clean_notes = []

    # Clean notes
    for n in notes:
        clean_notes.append(split_content(n))

    return clean_notes
