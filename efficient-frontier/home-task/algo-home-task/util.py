import json
import pandas as pd
from time import sleep
from matplotlib import pyplot as plt


def with_ijson(f):
    import ijson
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


def partial_json(fp, *, objs: int = None, until_key=None, lines: int = None, size=None) -> dict:
    if len([arg for arg in (objs, lines, until_key, size) if arg is not None]) != 1:
        raise ValueError("Specify exactly one parameter: either objs, lines, until_key or size.")
    if lines or size:
        raise NotImplementedError
    data: dict = json.load(fp)
    keys = list(data.keys())
    if objs:
        return {k: data[k] for k in keys[:objs]}
    if until_key:
        if data[until_key]:
            # spare O(n) by raising KeyError if doesn't exist
            pass
        dct = dict()
        for k, v in data.items():
            if k == until_key:
                return dct
            dct[k] = v


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


def plot(df:pd.DataFrame, title=None):
    return plotmany(df.index, [(df[col], dict(label=col.title())) for col in df.columns.format()], title)


def plotmany(x, objs, title=None):
    plt.figure(figsize=(15, 7))
    if title:
        # plt.title(title, color='white')
        plt.title(title)
    for obj, kwargs in objs:
        plt.plot(x, obj, **kwargs)
    plt.legend(loc='upper left')
    axes = plt.axes()
    axes.patch.set_facecolor('black')
    # plt.xticks(rotation=45,color='white')
    plt.xticks(rotation=45)
    # plt.yticks(color='white')
    plt.show()
