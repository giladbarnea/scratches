# with open('/home/gilad/.ipython/profile_default/startup/ipython_utils.py') as f:
#   exec(f.read())
import json

import pandas as pd
from matplotlib import pyplot as plt
import util
datafile = './data.json'


def main():
    with open('./data.json') as f:
        # 500ms~
        data: dict = json.load(f)
    chunk = util.get_chunks(data, chunksize=1000, chunk_count=1)[0]
    df = pd.DataFrame.from_dict(chunk, orient='index')
    # pyplot.figure(figsize=(12.5,4.5))
    plot = plt.plot(data=df[df.columns[0]])
    print()
    for df in util.simulate_stream(data):
        print(df)
    
    # df = pd.DataFrame.from_dict(data)  # 12s~


if __name__ == '__main__':
    main()
