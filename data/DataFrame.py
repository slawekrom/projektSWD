import numpy as np
import pandas as pd


class DataFrame:

    def __init__(self):
        self.df = None

    def change_to_number(self, column_name: str,
                         alphabetic_order: bool):  # true - alfabetyczne, false - według wystapienia
        values_list = self.df[column_name].unique().tolist()
        if alphabetic_order:
            values_list.sort()
        print(values_list)
        values_dict = {key: i for i, key in enumerate(values_list, start=1)}
        self.df[column_name] = self.df[column_name].map(values_dict)
        print(self.df.sample(2))

    def discretize(self, column_name: str, setsNumber):
        self.df[column_name + '_discrete'] = pd.cut(self.df[column_name], int(setsNumber))

    def normalize(self, column_name):
        self.df[column_name + '_norm'] = np.round_(
            (self.df[column_name] - self.df[column_name].mean()) / self.df[column_name].std(), decimals=3)

    def change_range(self, column_name, a, b):
        min = self.df[column_name].min()
        max = self.df[column_name].max()
        print(str(min) + ' ' + str(max))
        self.df[column_name + '_a_b'] = np.round_(((self.df[column_name] - min) / (max - min) * (b - a)) + a, decimals=
        3)

    def get_min_subset(self, column_name, percent: int):
        print(str(percent))
        self.sort(column_name)
        n = round(self.df.shape[0] * (percent / 100))
        return self.df.head(n)

    def get_max_subset(self, column_name, percent: int):
        self.sort(column_name)
        n = round(self.df.shape[0] * (percent / 100))
        return self.df.tail(n)

    def sort(self, column_name):
        self.df.sort_values(by=[column_name])
