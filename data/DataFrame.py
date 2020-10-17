class DataFrame:

    def __init__(self):
        self.df = None

    def change_to_number(self, column_name: str, alphabetic_order: bool): # true - alfabetyczne, false - według wystapienia
        values_list = self.df[column_name].unique().tolist()
        if alphabetic_order:
            values_list.sort()
        print(values_list)
        values_dict = {key: i for i, key in enumerate(values_list, start=1)}
        self.df[column_name] = self.df[column_name].map(values_dict)
        print(self.df.sample(2))
