import pandas as pd
import logging
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.info('Loading data...')
df = pd.read_csv(os.getenv('READ_PATH'), delimiter=';')
df.drop(columns=[df.columns[0]], inplace=True)
df['sku_quantity'].fillna(0, inplace=True)
df['sku_quantity'] = df['sku_quantity'].astype(int)
logging.info('Data loaded:')
print(df.info())
# drop duplicates
logging.info('Dropping duplicates...')
df.sort_values(by=['keyword', 'updatedat'], ascending=False, inplace=True)
df.drop_duplicates(subset=['keyword'], keep='first', inplace=True)
print(df.info())
# drop rows with search phrase length < 3 and > 256
logging.info('Dropping rows with search phrase length < 3 and > 256...')
df.drop(df[df['keyword'].str.len().gt(256)].index, inplace=True)
df.drop(df[df['keyword'].str.len().le(3)].index, inplace=True)
print(df.info())
print(df.describe())
# Calculate searchtimes for 30 days
logging.info('Calculating searchtimes for 30 days...')
df['searchtimes_7days'] = df['searchtimes'].astype(int)
df['searchtimes'] = df['searchtimes_7days'].apply(lambda x: int(x / 7 * 30))
df.sort_values(by=['searchtimes'], ascending=False, inplace=True)
# drop rows with searchtimes < 100
logging.info('Dropping rows with searchtimes < 50...')
df.drop(df[df['searchtimes'].le(50)].index, inplace=True)
print(df.describe())

# Write to file
logging.info('Writing to file...')
df.to_csv(os.getenv('SAVE_PATH'), sep=';', index=False, compression='gzip')
