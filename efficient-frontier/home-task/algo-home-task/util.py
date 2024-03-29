import json
from time import sleep
from typing import Tuple, List, Union, overload
from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt
import pickle
import json5

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


def json_load(path: str, new=False, dump_pickle=True) -> dict:
    """
    Tries to load data from pickle file. If pickle file doens't exist, loads original file.
    
    :param path: The file path, with or without extension, i.e. './output' or './output.pickle' or './output.json5'.
    :param new: Specify True to force using the original file and not use the pickled file.
    :param dump_pickle: By default, pickles the original file (if used). Specify False to not pickle even if original file is used.
    """
    
    def load_new():
        with open(jsonpath) as f:
            _data = jsonload(f)
        if dump_pickle:
            with open(picklepath, 'w+b') as f:
                pickle.dump(_data, f)
        return _data
    
    path = Path(path)
    if (tmp := path.with_suffix('.json5')).exists():
        jsonpath = tmp
        jsonload = json5.load
    else:
        jsonpath = path.with_suffix('.json')
        jsonload = json.load
    picklepath = path.with_suffix('.pickle')
    
    if new:
        # don't use pickle: load the actual file
        print(f'using original {jsonpath} and {"not " if not dump_pickle else ""}creating pickle')
        data = load_new()
        return data
    
    # use pickle if exists
    if picklepath.exists():
        print(f'using pickle: {picklepath}')
        with open(picklepath, 'r+b') as f:
            data = pickle.load(f)
            return data
    # pickle doesn't exist
    print(f"pickle doesn't exist: using original {jsonpath} and {'not ' if not dump_pickle else ''}creating pickle")
    data = load_new()
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


def plot(df: pd.DataFrame, *, title=None, figsize=(100, 20), linewidth=5):
    return plotmany(df.index, df, title=title, figsize=figsize, linewidth=linewidth)


@overload
def plotmany(index: pd.Index, data: List[Tuple[Data, dict]], *, title=None, figsize=(100, 20), linewidth=5):
    ...


@overload
def plotmany(index: pd.Index, data: List[Data], *, title=None, figsize=(100, 20), linewidth=5):
    ...


@overload
def plotmany(index: pd.Index, data: Data, *, title=None, figsize=(100, 20), linewidth=5):
    ...


def plotmany(index: pd.Index, data, *, title=None, figsize=(100, 20), linewidth=5):
    def _paint_df(_df: pd.DataFrame, _label=None, **_kwargs):
        for _col in _df.columns.format():
            if _label:
                _newlabel = f'{_label} - {_col.title()}'
            else:
                _newlabel = _col.title()
            if _df.isnull().values.any():
                _paint = plt.scatter
            else:
                _paint = plt.plot
            if 'marker' in _kwargs:
                _linewidth = 200
                _paint = plt.scatter
            else:
                _linewidth = linewidth
            _paint(index, _df[_col], label=_newlabel, linewidth=_linewidth, **_kwargs)
    
    def _ensure_df(_df_or_ser: Data) -> pd.DataFrame:
        if isinstance(_df_or_ser, pd.DataFrame):
            return _df_or_ser
        else:
            return _df_or_ser.to_frame()
    
    plt.figure(figsize=figsize)
    if title:
        # plt.title(title, color='white')
        plt.title(title, fontdict=dict(fontsize=70))
    if isinstance(data, (pd.DataFrame, pd.Series)):
        # e.g. plotmany(df.index, df)
        _paint_df(_ensure_df(data))
    else:
        # e.g. plotmany(df.index, [(df, {'label':'Foo'}), ...])
        for x in data:
            try:
                # data is a list of (df, {'label':'Foo'}) tuples
                df_or_ser, kwargs = x
            except ValueError:
                # data is a just a list of df or ser
                df_or_ser = x
                kwargs = dict()
            label = kwargs.pop('label', None)
            if isinstance(df_or_ser, (pd.DataFrame, pd.Series)):
                _paint_df(_ensure_df(df_or_ser), label, **kwargs)
            else:
                if df_or_ser.isnull().values.any():
                    paint = plt.scatter
                else:
                    paint = plt.plot
                paint(index, df_or_ser, label=label, **kwargs)
    plt.legend(loc='upper left', prop=dict(size=45))
    # plt.rcParams.update({'font.size': 22})
    axes = plt.axes()
    axes.patch.set_facecolor('black')
    # plt.xticks(rotation=45,color='white')
    plt.xticks(rotation=45)
    # plt.yticks(color='white')
    plt.grid(True, axis='y')
    plt.show()
