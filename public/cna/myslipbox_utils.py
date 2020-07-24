import copy
import re


def split_content(card):
    '''Split desc into 
       - text_md (main text in markdown)
       - links (linked notes)
       - quotes (linked quotes), and
       - sources (list of sources)
    '''

    card_new = copy.deepcopy(card)

    content = card_new['desc'].split('---')

    text_md = content[0]

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
