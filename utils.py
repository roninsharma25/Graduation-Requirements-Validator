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

def strFormatterECE(courses):
    """
    courses: list of courses
    """
    return ", ".join([ "ECE " + str(num) for num in courses ])

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
    # PHYS 1112, 2213, 2214 - TODO: INCORPORATE HONORS ALTERNATIVES
    # CHEM 2090
    # CS 1110
    for req in CLASS_SPECIFIC.keys():
        res = checkRequirement(data, req, 1)
        print(res)
        problems += res
    
    # TODO: ADD MULTI-OPTION CLASSES
    # Probability - 1 of ENGRD 2700, ECE 3100
    # Advanced Computing: 1 of CS 2110, ECE 2400, ENGRD 3200, AEP 4380, ECE 4740, ECE 4750, ECE 4760
    # CDE: 1 of 4370, 4530, 4670, 4740, 4750, 4760
    # Technical Writing: 1 of ENGRC 3350, ENGRC 3500, ENGRC 3023, ECE 4760 follow-up
        # TODO: check recent course addition

    return problems

def complicatedRequirements(data):
    problems = []

    # OTE -----
        # 9 credits
        # At least 1 3000+
        # No ENGRC, no ECE EXCEPT FOR ECE 5830
        # Provide a disclaimer: these should count/probably won't count
    requirementData = data.loc[['UPPER LEVEL']]
    classes = [class_.strip() for class_ in requirementData.iloc[0] if not pd.isnull(class_)]

    ECEClassesWithout5830 = [class_ for class_ in classes if class_.strip(' ')[0].upper() == 'ECE' and int(class_.strip(' ')[1]) != 5830 ]
    if ( len(ECEClassesWithout5830) > 0 ):
        problems.append(f'The only ECE course that can be considered an OTE is ECE 5830, but you have included these courses: {ECEClassesWithout5830}')

    ENGRCOTEClasses = [class_ for class_ in classes if class_.strip(' ')[0].upper() == 'ENGRC']
    if ( len(ENGRCOTEClasses) > 0 ):
        problems.append(f"ENGRC courses can't be used to satisfy the OTE reqirement, but you have included these courses: {ENGRCOTEClasses} ")

    OTE3000 = [ class_ for class_ in classes if ( int(class_.strip(' ')[1]) >= 3000 and class_ not in ENGRCOTEClasses ) ]
    if ( not len(OTE3000) ):
        problems.append('You need at least one 3000+ course as an OTE')

    # 3000/4000 - at least 21 credits -----
    # 3000 - at least 3
        # at least 3 of: 3030 or 3150, 3100 or 3250, or 3140
        # Not acceptable: 3600, 5830, 4999, 5870, 5880
    # 4000 (also count CDE) - at least 3
    requirementData = data.loc[['UPPER LEVEL']]
    classes = [class_.strip() for class_ in requirementData.iloc[0] if not pd.isnull(class_)]

    # Verify that all are ECE courses
    nonECEClasses = [class_ for class_ in classes if class_.strip(' ')[0].upper() != 'ECE']
    if (len(nonECEClasses) > 0):
        problems.append(f'All upper level courses need to be ECE courses, but you have included these courses: {nonECEClasses}')

    ECEClassNums = [class_.strip(' ')[1] for class_ in classes if class_.strip(' ')[0].upper() == 'ECE']
    invalidECEClasses = [num for num in ECEClassNums if num in INVALID_UPPER_LEVEL_ECE]
    if (len(invalidECEClasses) > 0):
        problems.append(f'The following courses are not acceptable upper-level ECE electives {invalidECEClasses}')
    
    foundationalCourses = [ class_ for class_ in ECEClassNums if class_ in ECE_FOUNDATION]
    if ( (3030 not in foundationalCourses) and (3150 not in foundationalCourses) ):
        problems.append('You need to take either ECE 3030 or ECE 3150')
    
    if ( (3100 not in foundationalCourses) and (3250 not in foundationalCourses) ):
        problems.append('You need to take either ECE 3100 or ECE 3250')
    
    if ( len(foundationalCourses) < 3 ):
        problems.append(f'You need to take at least three ECE foundational courses ({ strFormatterECE(ECE_FOUNDATION) })')

    # AAE
    requirementData = data.loc[['AAE']]
    classes = [class_.strip() for class_ in requirementData.iloc[0] if not pd.isnull(class_)]

    if ( len(classes) ):
        problems.append(f'Verify with your advisor that they approve of these courses as AAE: {classes}')
    else:
        problems.append(f'You have not taken any AAE classes')

    return problems

def analyzeData(uploadedFile):
    problems = []
    
    # TODO: the first non-header line shouldn't need to be the max length 
    fileData = pd.read_csv(uploadedFile, names = ['Category', 'Class 1', 'Class 2', 'Class 3', 'Class 4'], header = 0, index_col = 'Category')

    # Check LS requirement
    lsData = fileData.loc[['Liberal Studies']]
    lsClasses = [class_.strip() for class_ in lsData.iloc[0] if not pd.isnull(class_)]
    problems += analyzeLS(lsClasses)

    problems += simpleRequirements(fileData)
    problems += complicatedRequirements(fileData)

    print(fileData)
    print(f'Problems: {problems}')

    return fileData, problems

def analyzeLS(classes):
    problems = []
    df = pd.read_csv('liberal_studies.csv')
    
    # TODO: Update category checker logic not to double count single classes
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
