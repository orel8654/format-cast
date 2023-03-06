import pandas

def read():
    df = pandas.read_csv('/existing.csv', sep=';')
    data_dicts = df.to_dict('records')
    data_ids_phrases = list(set([i['search_phrase_id'] for i in data_dicts]))
    data_ids = [i['product_id'] for i in data_dicts]


    print(data_ids_phrases)

    data_c = [{i['product_id']: i['search_position']} for i in data_dicts if i['search_phrase_id'] == 4311543]

    for i in data_ids:
        if i == 672452958:
            print(i)

if __name__ == '__main__':
    read()