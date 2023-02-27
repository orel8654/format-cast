import os
import pandas

class ReadBigCSV:
    MAIN_COUNT = 0
    CHUNK = 10**5
    def __init__(self, path):
        with pandas.read_csv(path, chunksize=self.CHUNK, sep=';') as reader:
            for chunk in reader:
                MAIN_LIST = []
                df = pandas.DataFrame(chunk)
                _list = df.to_dict('records')
                for i in _list:
                    MAIN_LIST.append({
                        'created_at': i['2023-02-23 18:00:43.277183'],
                        'updated_at': i['2023-02-23 18:00:43.277183'],
                        'product_id': i['818012886'],
                        'search_phrase_id': i['4311546'],
                        'search_position': i['1'],
                    })
                self.MAIN_COUNT += len(MAIN_LIST)
                self.save(MAIN_LIST)

    def save(self, _list: list):
        df = pandas.DataFrame(_list)
        df.to_csv(os.getenv('SAVE_PATH'), mode='a', index=False, header=False, sep=';')
        print(self.MAIN_COUNT)

if __name__ == '__main__':
    w = ReadBigCSV(os.getenv('READ_PATH'))