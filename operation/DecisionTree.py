from pandas import DataFrame
import math
from collections import Counter
from data.Node import Node

class DecisionTree:

    def __init__(self, df):
        self.df: DataFrame = df
        self.mainEntropy = 0

    def calculate_main_entropy(self, df):
        counter = Counter(([element for element in df[df.columns[-1]]]))
        classes_count = df[df.columns[-1]].nunique()
        counter = counter.most_common(classes_count)
        rows = df.shape[0]
        mainEntropy = 0
        for i in range(len(counter)):
            mainEntropy+= self.calculate_entropy(round(counter[i][1]/rows,2))
        print(mainEntropy)
        self.mainEntropy = mainEntropy
        return mainEntropy


    def build_tree(self):
        mainEntropy = self.calculate_main_entropy(self.df)

        root: Node = Node('root', '', self.df)
        attributes_info_gain = dict()
        columns = self.df.columns[:-1]
        for column in columns:
            attributes_info_gain.update({column: self.calculate_attribute_entropy(column, self.df, mainEntropy)})

        best_attribute = max(attributes_info_gain, key=attributes_info_gain.get)
        values = self.df[best_attribute].unique().tolist()
        for value in values:
            tmp_df = self.df.loc[self.df[best_attribute] == value]
            classes = tmp_df[tmp_df.columns[-1]].nunique()
            if classes == 1: #obiekty jednej klasy - robimy liść
                node: Node = Node('leaf', '', tmp_df)
            else:
                tmp_df.drop([best_attribute])
                node: Node = Node('node', '', tmp_df)

    def calculate_entropy(self, p: float):
       return -p * math.log2(p)

    def calculate_attribute_entropy(self, column, df, mainEntropy):
        counter = Counter(([element for element in df[column]]))
        count = df[column].nunique()
        counter2 = counter.most_common(count)
        column_entropy = 0
        rows = df.shape[0]
        for i in range(len(counter)): #petla po wartościach
            tmp_df = df.loc[df[column] == counter.most_common(count)[i][0]]
            tmp_rows = tmp_df.shape[0]
            classes_count = tmp_df[tmp_df.columns[-1]].nunique()
            counter_classes = Counter(([element for element in tmp_df[tmp_df.columns[-1]]]))
            counter_classes = counter_classes.most_common(classes_count)

            for j in range(len(counter_classes)): # petla po klasach
                column_entropy+=(counter2[i][1]/rows) * self.calculate_entropy(round(counter_classes[j][1]/tmp_rows,2))

        info_gain = mainEntropy - column_entropy
        print(info_gain)
        return info_gain