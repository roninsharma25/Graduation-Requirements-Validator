from constants import *
import pandas as pd



def analyzeData(uploadedFile):
    problems = []

    # TODO: the first non-header line shouldn't need to be the max length 
    fileData = pd.read_csv(uploadedFile, names = ['Category', 'Class 1', 'Class 2', 'Class 3', 'Class 4'], header = 0, index_col = 'Category')

    # Check PE requirement
    fileData = fileData.loc[['PE']]

    peClasses = [class_.strip() for class_ in fileData.iloc[0] if not pd.isnull(class_)]
    numPEClasses = len(peClasses)
    print(peClasses)

    if (numPEClasses < NUM_PE):
        problems.append(f'You have not taken enough PE classes. You have only taken {numPEClasses}. You have only taken {", ".join(peClasses)}.')

    print(fileData)
    print(f'Problems: {problems}')
    return fileData