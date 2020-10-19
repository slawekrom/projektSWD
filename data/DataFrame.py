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
