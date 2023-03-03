import numpy as np
import pandas as pd
from pathlib import Path


input_data = Path.cwd().parent / 'Data' / 'small_data.csv'
output_data = Path.cwd().parent / 'Data' / r'output.txt'

df = pd.read_csv(input_data)
# print(df)

# add a json column to the dataframe
# splitlines will split the json into multiple rows not a single one
df['json'] = df.to_json(orient='records', lines=True).splitlines()
# print(df)

# just take the json column of the dataframe
df_json = df['json']
# print(df_json)

# print out the dataframe to a file
# Note that the timestamp forward slash will be escaped to stay true to JSON schema
np.savetxt(output_data, df_json.values, fmt='%s')
