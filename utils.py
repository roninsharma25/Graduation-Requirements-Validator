import pandas as pd


def analyzeData(uploadedFile):
    fileData = pd.read_csv(uploadedFile)
    print(fileData)
    return fileData