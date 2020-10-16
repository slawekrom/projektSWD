from operation.FileLoader import FileLoader

def main():
    file_loader: FileLoader = FileLoader()
    df = file_loader.loadFile("iris.txt", "\t")
    print(df)
    print(df.columns)


if __name__ == '__main__':
    main()