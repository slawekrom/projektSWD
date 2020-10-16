import pandas as pd
import numpy as np


class FileLoader:

    def loadFile(self, file_path: str, separator: str):
        df = pd.read_csv(file_path, sep=separator, index_col=0)
        return df
