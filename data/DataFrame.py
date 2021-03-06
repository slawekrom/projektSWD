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

    def add_to_number(self, column_name: str,
                         alphabetic_order: bool):  # true - alfabetyczne, false - według wystapienia
        values_list = self.df[column_name].unique().tolist()
        if alphabetic_order:
            values_list.sort()
        print(values_list)
        values_dict = {key: i for i, key in enumerate(values_list, start=1)}
        self.df.insert(len(self.df.columns), column_name + ": numeric", self.df[column_name].map(values_dict), True)
        print(self.df.sample(2))

    def discretize(self, column_name: str, setsNumber, new_column:bool):
        labels = []
        fract = round(1/int(setsNumber),2)
        labels.append(0)
        for i in range(1, int(setsNumber)):
            element = i*fract
            labels.append(element)

        labels.append(1)

        if new_column:
            self.df[column_name + '_discrete'] = pd.qcut(self.df[column_name],q=labels,
                            labels=False,
                            precision=0)
        else:
            self.df[column_name] = pd.qcut(self.df[column_name], q=labels,
                                                         labels=False,
                                                         precision=0)

    def normalize(self, column_name):
        self.df[column_name + '_normalize'] = np.round_(
            (self.df[column_name] - self.df[column_name].mean()) / self.df[column_name].std(), decimals=3)

    def normalize_all(self):
        columns_list = self.df.columns

        for i in range(len(columns_list) - 1):
            self.df[columns_list[i] + '_normalize'] = np.round_(
                (self.df[columns_list[i]] - self.df[columns_list[i]].mean()) / self.df[columns_list[i]].std(),
                decimals=3)

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

    def append(self, values: str, object_class):
        values_array = np.array(values.split(" ")).astype(np.float)
        new_object = np.append(values_array, 0.0)
        self.df.loc[len(self.df)] = new_object
        columns = self.df.columns
        self.df.at[len(self.df) - 1, columns[len(columns) - 1]] = object_class

    def sort(self, column_name):
        self.df.sort_values(by=[column_name])
