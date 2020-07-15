import json
from typing import Tuple, List, Union, overload

import pandas as pd
from time import sleep
from matplotlib import pyplot as plt

Data = Union[pd.DataFrame, pd.Series]


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


def plot(df: pd.DataFrame, *, title=None):
    return plotmany(df.index, df, title=title)


@overload
def plotmany(index: pd.Index, data: List[Tuple[Data, dict]], *, title=None):
    ...


@overload
def plotmany(index: pd.Index, data: Data, *, title=None):
    ...


def plotmany(index: pd.Index, data, *, title=None):
    def _plot_df(_df: pd.DataFrame, _label=None, **_kwargs):
        for _col in _df.columns.format():
            if _label:
                _newlabel = f'{_label} - {_col.title()}'
            else:
                _newlabel = _col.title()
            plt.plot(index, _df[_col], label=_newlabel, **_kwargs)
    
    plt.figure(figsize=(15, 7))
    if title:
        # plt.title(title, color='white')
        plt.title(title)
    if isinstance(data, pd.DataFrame):
        _plot_df(data)
    else:
        for df_or_ser, kwargs in data:
            label = kwargs.pop('label', None)
            if isinstance(df_or_ser, pd.DataFrame):
                _plot_df(df_or_ser, label, **kwargs)
            else:
                plt.plot(index, df_or_ser, label=label, **kwargs)
    plt.legend(loc='upper left')
    axes = plt.axes()
    axes.patch.set_facecolor('black')
    # plt.xticks(rotation=45,color='white')
    plt.xticks(rotation=45)
    # plt.yticks(color='white')
    plt.show()
