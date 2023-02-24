import pandas

class ReadBigCSV:
    MAIN_LIST = []
    CHUNK = 10
    def __init__(self, path):
        with pandas.read_csv(path, chunksize=self.CHUNK, sep=';') as reader:
            for chunk in reader:
                df = pandas.DataFrame(chunk)
                _list = df.to_dict('records')
                self.MAIN_LIST.extend([i for i in _list])

if __name__ == '__main__':
    w = ReadBigCSV('/Users/egororlov/Desktop/existing.csv')