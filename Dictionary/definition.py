import pandas as pd
import requests

data = requests.get

class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv('/home/xuanhien/PycharmProjects/PythonLearning/Dictionary/data.csv')
        return tuple(df.loc[df['word'] == self.term]['definition'])


d = Definition(term='is part of theme')
print(d.get())
