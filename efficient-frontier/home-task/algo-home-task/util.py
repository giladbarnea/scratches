import json
import ijson
import pandas as pd
from time import sleep


def with_ijson(f):
    parser = ijson.parse(f)
    start_new_state = False
    data = dict()
    for prefix, event, value in parser:
        if event == 'map_key' and prefix == '' and value is not None:
            # next iteration will be the beginning of a new state (new timestamp)
            start_new_state = True
            continue
        
        if start_new_state:
            ts = prefix
            # initialize state
            data[ts] = dict(assetA=dict(ask=None, bid=None), assetB=dict(ask=None, bid=None))
            start_new_state = False
            continue
        
        if prefix.endswith('.ask') or prefix.endswith('.bid'):
            # i.e. '1577836803078.assetA.ask'
            # set value for given ask / bid
            _, asset, order = prefix.split('.')
            data[ts][asset][order] = value
    return data


def with_json(f):
    return json.load(f)


def get_chunks(data, chunksize=10000, chunk_count=None):
    chunks = []
    chunk = dict()
    count = 0
    for i, (key, value) in enumerate(data.items()):
        if i and i % chunksize == 0:
            chunks.append(chunk)
            count += 1
            chunk = dict()
            if chunk_count and chunk_count == count:
                return chunks
        chunk[key] = value
    return chunks


def simulate_stream(data):
    """Yields a DataFrame"""
    keys = list(data.keys())
    for i, (key, value) in enumerate(data.items()):
        try:
            yield pd.DataFrame({key: value})
            nextkey = int(keys[i + 1])
            diff_sec = (nextkey - int(key)) / 1000
            sleep(diff_sec)
        except IndexError:
            # end of file
            return
