import math
import numpy as np
from collections import Counter

class Metrics:

    def __init__(self, size, dataframe):
        self.euclidean_distance = [[0 for i in range(size)] for j in range(size)]
        self.manhattan_distance = [[0 for i in range(size)] for j in range(size)]
        self.chebyshev_distance = [[0 for i in range(size)] for j in range(size)]
        self.df = dataframe

    def calculate_euclidean(self, size):
        column_count = len(self.df.columns)
        columns = []
        columns = self.df.columns
        for i in range(size):
            for j in range(i):
                sum = 0
                for k in range(column_count - 1):
                    sum += math.pow((self.df.at[i, columns[k]] - self.df.at[j, columns[k]]), 2)
                self.euclidian_distance[i][j] = math.sqrt(sum)

        for row in self.euclidean_distance:
            print(row)

    def calculate_manhattan(self, size):
        column_count = len(self.df.columns)
        columns = []
        columns = self.df.columns
        for i in range(size):
            for j in range(i):
                sum = 0
                for k in range(column_count - 1):
                    sum += math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]])
                self.manhattan_distance[i][j] = sum

        for row in self.manhattan_distance:
            print(row)


    def calculate_chebyshev(self, size):
        column_count = len(self.df.columns)
        columns = []
        columns = self.df.columns
        for i in range(size):
            for j in range(i):
                sum = 0
                for k in range(column_count - 1):
                    if math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]]) > sum:
                        sum = math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]])
                self.chebyshev_distance[i][j] = sum

        for row in self.chebyshev_distance:
            print(row)

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

