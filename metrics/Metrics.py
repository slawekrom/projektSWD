import math
import numpy as np
from collections import Counter
from metrics.Distance import Distance

class Metrics:

    def __init__(self, size, dataframe):
        self.euclidean_distance = [[0 for i in range(size)] for j in range(size)]
        self.manhattan_distance = [[0 for i in range(size)] for j in range(size)]
        self.chebyshev_distance = [[0 for i in range(size)] for j in range(size)]
        self.df = dataframe
        self.size = size

    def calculate_euclidean(self):
        column_count = len(self.df.columns)
        columns = []
        columns = self.df.columns
        for i in range(self.size):
            for j in range(i):
                sum = 0
                for k in range(column_count - 1):
                    sum += math.pow((self.df.at[i, columns[k]] - self.df.at[j, columns[k]]), 2)
                    distance: Distance = Distance(math.sqrt(sum), i, j)
                self.euclidean_distance[i][j] = distance

        #print(self.euclidean_distance)

    def classify_euclidean(self):
        self.calculate_euclidean()
        counter: Counter
        columns = []
        columns = self.df.columns
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size): # i to wiersz danych
            distance_list = [row[i] for row in self.euclidean_distance]
            distance_list = distance_list[i+1: self.size] + self.euclidean_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, columns[len(self.df.columns) - 1]]
            for k in range(self.size - 1): # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, columns[len(self.df.columns) - 1]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] +=1


        print(k_classify)

    def classify_manhattan(self):
        self.calculate_manhattan()
        counter: Counter
        columns = []
        columns = self.df.columns
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size): # i to wiersz danych
            distance_list = [row[i] for row in self.manhattan_distance]
            distance_list = distance_list[i+1: self.size] + self.manhattan_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, columns[len(self.df.columns) - 1]]
            for k in range(self.size - 1): # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, columns[len(self.df.columns) - 1]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] +=1


        print(k_classify)

    def classify_chebyshev(self):
        self.calculate_chebyshev()
        counter: Counter
        columns = []
        columns = self.df.columns
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size): # i to wiersz danych
            distance_list = [row[i] for row in self.chebyshev_distance]
            distance_list = distance_list[i+1: self.size] + self.chebyshev_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, columns[len(self.df.columns) - 1]]
            for k in range(self.size - 1): # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, columns[len(self.df.columns) - 1]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] +=1


        print(k_classify)

    def calculate_manhattan(self):
        column_count = len(self.df.columns)
        columns = []
        columns = self.df.columns
        for i in range(self.size):
            for j in range(i):
                sum = 0
                for k in range(column_count - 1):
                    sum += math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]])
                distance: Distance = Distance(sum, i, j)
                self.manhattan_distance[i][j] = distance

        # for row in self.manhattan_distance:
        #     print(row)


    def calculate_chebyshev(self):
        column_count = len(self.df.columns)
        columns = []
        columns = self.df.columns
        for i in range(self.size):
            for j in range(i):
                sum = 0
                for k in range(column_count - 1):
                    if math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]]) > sum:
                        sum = math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]])
                distance: Distance = Distance(sum, i, j)
                self.chebyshev_distance[i][j] = distance

        # for row in self.chebyshev_distance:
        #     print(row)

    @staticmethod
    def manhattan_distance(values: str, df, k: int):
        values_array = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = []
        columns = df.columns
        distance = dict()
        for j in range(len(df.index)):
            sum = 0
            for n in range(column_count - 1):
                sum += math.fabs(values_array[n] - df.at[j, columns[n]])
            distance[j] = sum

        print(distance)
        list_of_knn = list()
        for w in sorted(distance, key=distance.get, reverse=False):
            list_of_knn.append(df.at[w, columns[len(df.columns) - 1]])
            if len(list_of_knn) == k:
                break
        print(list_of_knn)
        counter: Counter = Counter(([element for element in list_of_knn]))
        print(counter.most_common(1)[0][0])
        return counter.most_common(1)[0][0]

    @staticmethod
    def euclidean_distance(values: str, df, k: int):
        values_array = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = []
        columns = df.columns
        distance = dict()
        for j in range(len(df.index)):
            sum = 0
            for n in range(column_count - 1):
                sum += math.pow((values_array[n] - df.at[j, columns[n]]), 2)
            distance[j] = math.sqrt(sum)

        print(distance)
        list_of_knn = list()
        for w in sorted(distance, key=distance.get, reverse=False):
            list_of_knn.append(df.at[w, columns[len(df.columns) - 1]])
            print(w)
            if len(list_of_knn) == k:
                break

        print('knn ' + str(list_of_knn))
        counter: Counter = Counter(([element for element in list_of_knn]))
        print(counter.most_common(1)[0][0])
        return counter.most_common(1)[0][0]

    @staticmethod
    def chebyshev_distance(values: str, df, k: int):
        values_array = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = []
        columns = df.columns
        distance = dict()
        for j in range(len(df.index)):
            sum = 0
            for n in range(column_count - 1):
                if math.fabs(values_array[n] - df.at[j, columns[n]]) > sum:
                    sum = math.fabs(values_array[n] - df.at[j, columns[n]])
            distance[j] = sum

        print(distance)
        list_of_knn = list()
        for w in sorted(distance, key=distance.get, reverse=False):
            list_of_knn.append(df.at[w, columns[len(df.columns) - 1]])
            if len(list_of_knn) == k:
                break
        print(list_of_knn)
        counter: Counter = Counter(([element for element in list_of_knn]))
        print(counter.most_common(1)[0][0])
        return counter.most_common(1)[0][0]

