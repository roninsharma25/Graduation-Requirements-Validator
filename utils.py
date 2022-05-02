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

def checkRequirement(data, requirement, type_):
    """
    type: 0 for minimum number, 1 for specific classes
    
    """
    requirementData = data.loc[[requirement]]
    classes = [class_.strip() for class_ in requirementData.iloc[0] if not pd.isnull(class_)]
    problems = []

    if (type_ == 0):

        requiredNum = MIN_NUMBER[requirement]
        if (len(classes) < requiredNum):
            problems.append(f'You have not taken enough {requirement} classes. You have taken {", ".join(classes)}, but need to take {requiredNum}.')
    
    else: # type 1
        classNums = [class_.strip(' ')[-1] for class_ in classes]
        missingClasses = [class_ for class_ in CLASS_SPECIFIC[requirement] if class_ not in classNums]
        if (missingClasses != []):
            problems.append(f'You have not taken all {requirement} classes. You have taken {", ".join(classes)}, but need to take {missingClasses}.')

    return problems

def simpleRequirements(data):

    problems = []

    # 2 PE
    # 1 ENGRI
    # 2 FWS
    # 1 ENGRD
    # ECE 2100, 2200, 2300
    for req in ['PE', 'ENGRI', 'FWS', 'ENGRD']:
        problems += checkRequirement(data, req, 0)
    
    # MATH 1910, 1920, 2930, 2940
    # PHYS 1112, 2213, 2214
    # CHEM 2090
    # CS 1110
    for req in CLASS_SPECIFIC.keys():
        res = checkRequirement(data, req, 1)
        print(res)
        problems += res

    return problems

def complicatedRequirements():
    # CDE

    # Advanced computing

    # Probability

    # OTE

    # 3000/4000/AAE

    pass


def analyzeData(uploadedFile):
    problems = []
    
    # TODO: the first non-header line shouldn't need to be the max length 
    fileData = pd.read_csv(uploadedFile, names = ['Category', 'Class 1', 'Class 2', 'Class 3', 'Class 4'], header = 0, index_col = 'Category')

    # Check LS requirement
    lsData = fileData.loc[['Liberal Studies']]
    lsClasses = [class_.strip() for class_ in lsData.iloc[0] if not pd.isnull(class_)]
    problems += analyzeLS(lsClasses)

    problems += simpleRequirements(fileData)

    print(fileData)
    print(f'Problems: {problems}')

    return fileData

def analyzeLS(classes):
    problems = []
    df = pd.read_csv('liberal_studies.csv')
    
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

    return problems