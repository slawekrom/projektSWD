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
        counter = counter.most_common(classes_count) #licznik klas
        rows = df.shape[0]
        mainEntropy = 0
        for i in range(len(counter)):
            mainEntropy+= self.calculate_entropy(round(counter[i][1]/rows,2))
        print('main entropy ' + str(mainEntropy))
        self.mainEntropy = mainEntropy
        return mainEntropy


    def build_tree(self):
        mainEntropy = self.calculate_main_entropy(self.df)

        root: Node = Node('root', '', self.df)
        root.add_children(self.make_node(self.df, mainEntropy))
        # attributes_info_gain = dict()
        # columns = self.df.columns[:-1]
        # for column in columns:
        #     attributes_info_gain.update({column: self.calculate_attribute_entropy(column, self.df, mainEntropy)})
        #
        # best_attribute = max(attributes_info_gain, key=attributes_info_gain.get)
        # values = self.df[best_attribute].unique().tolist()
        # for value in values:
        #     tmp_df = self.df.loc[self.df[best_attribute] == value]
        #     classes = tmp_df[tmp_df.columns[-1]].nunique()
        #     if classes == 1: #obiekty jednej klasy - robimy liść
        #         node: Node = Node('leaf', '', tmp_df)
        #     else:
        #         tmp_df.drop([best_attribute])
        #         node: Node = Node('node', '', tmp_df)

    def make_node(self, df: DataFrame, mainEntropy):
        nodes = list()
        attributes_info_gain = dict()
        columns = df.columns[:-1]
        for column in columns:
            attributes_info_gain.update({column: self.calculate_attribute_entropy(column, df, mainEntropy)})

        best_attribute = max(attributes_info_gain, key=attributes_info_gain.get)
        values = df[best_attribute].unique().tolist()
        if attributes_info_gain.get(best_attribute) <0.05: #jeśli info gain mniejsze niż 0,05 nie ma sensu dzielić
            return None # przerywam wykonane funkcji
        for value in values:
            tmp_df = df.loc[df[best_attribute] == value]
            classes = tmp_df[tmp_df.columns[-1]].nunique()
            if classes == 1 or len(columns) == 1:  # obiekty jednej klasy - robimy liść
                node: Node = Node('leaf', '', tmp_df)
                nodes.append(node)
            else:
                tmp_df = tmp_df.drop([best_attribute], axis=1)
                node: Node = Node('node', '', tmp_df)
                node_main_entropy = self.calculate_main_entropy(tmp_df)
                children_nodes = self.make_node(tmp_df, node_main_entropy)
                if children_nodes == None: # z aktualnego węzła robimy liść
                    counter = Counter(([element for element in tmp_df[df.columns[-1]]]))
                    node = Node('leaf', '', tmp_df, node_class=counter.most_common(1)[0][0])
                    nodes.append(node)
                else:
                    node.add_children(children_nodes)
                    nodes.append(node)

        return nodes

    def calculate_entropy(self, p: float):
       return -p * math.log2(p)

    def calculate_attribute_entropy(self, column, df, mainEntropy):
        counter = Counter(([element for element in df[column]])) # licznik wartości atrybutu
        count = df[column].nunique()
        counter2 = counter.most_common(count) # licznik wartości atrybutu posortowany
        column_entropy = 0
        rows = df.shape[0]
        for i in range(len(counter)): #petla po wartościach 0,1 ...
            tmp_df = df.loc[df[column] == counter.most_common(count)[i][0]]
            tmp_rows = tmp_df.shape[0]
            classes_count = tmp_df[tmp_df.columns[-1]].nunique()
            counter_classes = Counter(([element for element in tmp_df[tmp_df.columns[-1]]]))
            counter_classes = counter_classes.most_common(classes_count)

            for j in range(len(counter_classes)): # petla po klasach
                column_entropy+=(counter2[i][1]/rows) * self.calculate_entropy(round(counter_classes[j][1]/tmp_rows,2))

        info_gain = mainEntropy - column_entropy
        print('info gain atribute' + column + ' ' + str(info_gain))
        return info_gain