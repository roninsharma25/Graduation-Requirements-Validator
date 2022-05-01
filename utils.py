from constants import *
import pandas as pd
import numpy as np

"""
Features to check
1. MATH, PHYS, CHEM, CS, PE, FWS, ENGRI, ENGRD
2. Liberal studies
3. 2100, 2200, 2300
4. AAE
5. OTE
6. 3000+ ECE
7. 4000+ ECE
8. CDE
9. Advanced computing
10. Probability

"""

problems = []

def basicRequirements():
    # MATH 1910, 1920, 2930, 2940

    # PHYS 1112, 2213, 2214

    # CHEM 2090

    # CS 1110

    # 2 PE

    # 1 ENGRI

    # 1 ENGRD

    # 2 FWS

    pass

def eceSpecific():
    # ECE 2100, 2200, 2300

    # CDE

    # Advanced computing

    # Probability

    # OTE

    # 3000/4000/AAE

    pass


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