import urllib2
import urllib
import datetime
import csv

url = "http://ichart.finance.yahoo.com/x?{0}"

def get_url_path(symbol, start=None, end=None, provider='yahoo'):
    if start is None:
        start = datetime.datetime(1970,1,1)
    if end is None:
        end = datetime.datetime.today()

    assert isinstance(start, datetime.datetime)
    assert isinstance(end, datetime.datetime)

    start = start.strftime('%Y-%m-%d')
    end = end.strftime('%Y-%m-%d')

    date_bits = start.split('-') + end.split('-')
    date_bits = zip(('a','b','c','d','e','f'), date_bits)

    q = dict(date_bits)
    q['s'] = symbol
    # not sure what these are. Hardcoded from quantmod
    q['g'] = 'v'
    q['y'] = 0
    q['z'] = 30000
    qs = urllib.urlencode(q)

    return url.format(qs)

def parse_splits(rows):
    splits = []
    for row in rows:
        if row[0] != 'SPLIT':
            continue
        date = datetime.datetime.strptime(row[1].strip(), '%Y%m%d')
        split_to, split_from = row[2].split(':')
        splits.append((date, int(split_to), int(split_from)))
    return splits

def get_splits(symbol, start=None, end=None, provider='yahoo'):
    assert provider == 'yahoo'

    url = get_url_path(symbol, start, end, provider) 
    resp = urllib2.urlopen(url)
    data = list(csv.reader(resp))[1:]
    return parse_splits(data)

