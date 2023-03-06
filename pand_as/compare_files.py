import pandas

def read():
    df = pandas.read_csv('/existing.csv', sep=';')
    data_dicts = df.to_dict('records')
    data_ids = [i['product_id'] for i in data_dicts]
    for i in data_ids:
        if i == 672452958:
            print(i)

if __name__ == '__main__':
    read()