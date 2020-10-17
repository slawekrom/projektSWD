import pandas as pd
import numpy as np


class FileLoader:

    def loadFile(self, file_path: str, separator: str, col_index):
        df = pd.read_csv(file_path, separator, index_col=None)
        return df
