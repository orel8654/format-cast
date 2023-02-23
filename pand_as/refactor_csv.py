import pandas
import os

class RefactorPandas:
    def __init__(self, path):
        self.df = pandas.read_csv(path)

    def delete_cols(self, cols: list):
        for name_cols in cols:
            self.df.drop(name_cols, axis=1, inplace=True)

    def save_file(self):
        file_name = 'ozon_kw_res_join.csv'
        self.df.to_csv(file_name, sep=';', index=False)

if __name__ == '__main__':
    wr = RefactorPandas(path=os.getenv('READ_PATH'))
    wr.delete_cols(['searchtimes_7days'])
    wr.save_file()