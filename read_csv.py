import pandas
import csv

class Reader:
    def __init__(self, file_path : str, step=None):
        self.file_path = file_path
        self.step = step
        self.delimiter = self.find_delimiter()

    def find_delimiter(self):
        sniffer = csv.Sniffer()
        with open(self.file_path) as fp:
            delimiter = sniffer.sniff(fp.read(5000)).delimiter
        return delimiter

    def read_csv(self):
        self.data_frame = pandas.read_csv(self.file_path, sep=self.delimiter)

    def delete_columns(self, cols : list):
        for col in cols:
            self.data_frame.drop(col, axis=1, inplace=True)

    def delete_rows(self):
        dict = self.data_frame.to_dict('records')
        indexes_removed = []
        for i in range(len(dict)):
            if len(dict[i]['keyword']) > 256:
                indexes_removed.append(i)
        for idx in indexes_removed:
            del dict[idx]
        self.data_frame = pandas.DataFrame(dict)

    def type_casting(self, cols : list):
        for col in cols:
            self.data_frame[col] = self.data_frame[col].astype(dtype=int, errors='ignore')

    def write_csv(self, path : str):
        if self.step is None:
            file_name = 'ozon_kw_res.csv'
            self.data_frame.to_csv(path+file_name, sep=',', index=False)
        else:
            for iter in range((len(self.data_frame) // self.step) + 1):
                file_name = f'ozon_kw_res{iter + 1}.csv'
                self.data_frame[(self.step * ((iter+1) - 1)) if iter != 0 else 0:(self.step * (iter + 1))].to_csv(path + file_name, sep=',', index=False)

if __name__ == '__main__':
    r = Reader('/Users/macbook/Desktop/ozon_kw.csv')
    r.read_csv()
    r.delete_columns(['ii', 'searchtimes_7days'])
    r.type_casting(['sku_quantity'])
    r.write_csv('/Users/macbook/Desktop/')