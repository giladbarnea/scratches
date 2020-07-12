# with open('/home/gilad/.ipython/profile_default/startup/ipython_utils.py') as f:
#   exec(f.read())
from collections import defaultdict
from typing import List

import pandas as pd
import json
import ijson
from time import sleep

datafile = './data.json'


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


def chunk_dfs(data) -> List[pd.DataFrame]:
    dfs = []
    chunk = dict()
    for i, (key, value) in enumerate(data.items()):
        if i % 10000 == 0:
            df = pd.DataFrame(chunk)
            dfs.append(df)
            chunk = dict()
            print(f'created df #{len(dfs)}')
        chunk[key] = value
    return dfs


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


def main():
    with open('./data.json') as f:
        # 500ms~
        data: dict = json.load(f)
    for df in simulate_stream(data):
        print(df)
    
    # df = pd.DataFrame.from_dict(data)  # 12s~


if __name__ == '__main__':
    main()
