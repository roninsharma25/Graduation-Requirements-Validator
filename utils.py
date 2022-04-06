from constants import *
import pandas as pd
import numpy as np

problems = []

def analyzeData(uploadedFile):
    global problems
    
    # TODO: the first non-header line shouldn't need to be the max length 
    fileData = pd.read_csv(uploadedFile, names = ['Category', 'Class 1', 'Class 2', 'Class 3', 'Class 4'], header = 0, index_col = 'Category')

    # Check PE requirement
    peData = fileData.loc[['PE']]

    peClasses = [class_.strip() for class_ in peData.iloc[0] if not pd.isnull(class_)]
    numPEClasses = len(peClasses)
    print(peClasses)

    if (numPEClasses < NUM_PE):
        problems.append(f'You have not taken enough PE classes. You have only taken {numPEClasses}. You have only taken {", ".join(peClasses)}.')

    # Check LS requirement
    lsData = fileData.loc[['Liberal Studies']]
    lsClasses = [class_.strip() for class_ in lsData.iloc[0] if not pd.isnull(class_)]
    analyzeLS(lsClasses)

    print(fileData)
    print(f'Problems: {problems}')

    return fileData

def analyzeLS(classes):
    global problems
    df = pd.read_csv('liberal_studies.csv')

    print(classes)
    
    # TODO: Update category checker logic nto to double count single classes
    categories = []
    for class_ in classes:
        print(class_)
        categories += [category for category in df[ df['Department + Course Number'] == class_].iloc[:, 0]]
    
    # Remove redundant categories
    categories = np.unique(categories)

    numLSCategories = len(categories)
    if (numLSCategories < NUM_LS_CAT):
        problems.append(f'You have not taken enough LS categories. You have only taken {categories}, but you need {NUM_LS_CAT} categories.')

    
    print()
    print('CATEGORIES: ', np.unique(categories))