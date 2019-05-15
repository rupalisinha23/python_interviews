import json
from pandas.io.json import json_normalize
import pandas as pd

with open(r'data\abc.json') as data_file:
    data = json.load(data_file)


df = json_normalize(data, 'locations', ['date', 'number', 'name'],
                    record_prefix='locations_')
for i, x in df.iterrows():
    print(" | ".join(tuple(x)))

df2 = pd.read_json(r'data\abc.json', orient='records')
for i, x in df2.iterrows():
    print(tuple(x))

with open(r'data\abc.json') as data_file:
    data = json.load(data_file)
    df3 = pd.DataFrame(data)
    for i, x in df3.iterrows():
        print(x)
