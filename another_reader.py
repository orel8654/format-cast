import pandas

class Read_Write_S:
    def __init__(self):
        self.replacement_dict = {
            '\\\\n': ' ',
            '\"': ' ',
            ';': ' ',
            '\"\"': ' ',
            '\\\\': ' ',
        }

    def call(self):
        df = pandas.read_csv('/Users/macbook/Desktop/ozon_kw.csv')
        df['keyword'] = df['keyword'].replace(self.replacement_dict, regex=True)
        df['keyword'] = df['keyword'].str.strip()
        df_n = df.drop(['ii', 'searchtimes_7days'], axis=1)
        df_n.reset_index()
        df_r = df_n.loc[df_n['keyword'].str.len() <= 255]
        df_r.to_csv('COMPLETE_KW_FILE.csv', index=False)

if __name__ == '__main__':
    r = Read_Write_S()
    r.call()