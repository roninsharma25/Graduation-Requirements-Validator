from constants import *
import pandas as pd
import numpy as np


def strFormatter(courses, subj):
    """
    courses: list of courses
    subj: course subject
    """
    return ", ".join([ f"{subj} " + str(num) for num in courses ])

def checkRequirement(data, requirement, type_):
    """
    type: 0 for minimum number, 1 for specific classes
    """
    requirementData = data.loc[[requirement]]
    classes = [class_.strip() for class_ in requirementData.iloc[0] if not pd.isnull(class_)]
    problems = []

    if (type_ == 0):

        requiredNum = MIN_NUMBER[requirement]
        numTaken = len(classes)
        if (numTaken < requiredNum):
            str_ = f'You have not taken enough {requirement} classes. '
            if (numTaken == 0):
                str_ += f'You need to take {requiredNum}.'
            else:
                str_ += f'You have taken {", ".join(classes)}, but need to take {requiredNum}.'
            
            problems.append(str_)
    
    elif (type_ == 1):
        classNums = [int(class_.split(' ')[-1]) for class_ in classes]
        missingClasses = [class_ for class_ in CLASS_SPECIFIC[requirement] if class_ not in classNums]
        if (missingClasses != []):
            str_ = f'You have not taken all {requirement} classes. '
            missingFormatted = strFormatter(missingClasses, REQUIREMENT_MAPPER[requirement])
            if (len(classNums) == 0):
                str_ += f'You need to take {missingFormatted}.'
            else:
                str_ += f'You have taken {", ".join(classes)}, but need to take {missingFormatted}.'
            
            problems.append(str_)
    
    else: # type 2
        possibleClasses = MULTI_OPTION[requirement]
        flag = True

        for class_ in classes:
            if class_ in possibleClasses:
                flag = False

        if (flag):
            problems.append(f'You have not taken at least one {requirement} course. Here ' +
            f'are some options: {", ".join(possibleClasses)}.')

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
        problems += checkRequirement(data, req, 1)
    
    # Probability - 1 of ENGRD 2700, ECE 3100
    # Advanced Computing: 1 of CS 2110, ECE 2400, ENGRD 3200, AEP 4380, ECE 4740, ECE 4750, ECE 4760
    # CDE: 1 of 4370, 4530, 4670, 4740, 4750, 4760
    # Technical Writing: 1 of ENGRC 3350, ENGRC 3500, ENGRC 3023,
    for req in MULTI_OPTION.keys():
        problems += checkRequirement(data, req, 2)

    return problems

def complicatedRequirements(data):
    problems = []

    # OTE -----
        # 9 credits
        # At least 1 3000+
        # No ENGRC, no ECE EXCEPT FOR ECE 5830
        # Provide a disclaimer: these should count/probably won't count
    requirementData = data.loc[['OTE']]
    classes = [class_.split() for class_ in requirementData.iloc[0] if not pd.isnull(class_)]

    print(classes)
    ECEClassesWithout5830 = [class_ for class_ in classes if class_[0].strip().upper() == 'ECE' and int(class_[1]) != 5830 ]
    if ( len(ECEClassesWithout5830) > 0 ):
        problems.append(f'The only ECE course that can be considered an OTE is ECE 5830, but you have included these courses: {ECEClassesWithout5830}.')

    ENGRCOTEClasses = [class_ for class_ in classes if class_[0].strip().upper() == 'ENGRC']
    if ( len(ENGRCOTEClasses) > 0 ):
        problems.append(f"ENGRC courses can't be used to satisfy the OTE reqirement, but you have included these courses: {ENGRCOTEClasses}.")

    OTE3000 = [ class_ for class_ in classes if ( int(class_[1]) >= 3000 and class_ not in ENGRCOTEClasses ) ]
    if ( not len(OTE3000) ):
        problems.append('You need at least one 3000+ course as an OTE.')

    # 3000/4000 - at least 21 credits -----
    # 3000 - at least 3
        # at least 3 of: 3030 or 3150, 3100 or 3250, or 3140
        # Not acceptable: 3600, 5830, 4999, 5870, 5880
    # 4000 (also count CDE) - at least 3
    requirementData = data.loc[['UPPER LEVEL']]
    classes = [class_.split() for class_ in requirementData.iloc[0] if not pd.isnull(class_)]

    # Verify that all are ECE courses
    nonECEClasses = [class_ for class_ in classes if class_[0].strip().upper() != 'ECE']
    if (len(nonECEClasses) > 0):
        problems.append(f'All upper level courses need to be ECE courses, but you have included these courses: {nonECEClasses}.')

    ECEClassNums = [int(class_[1]) for class_ in classes if class_[0].strip().upper() == 'ECE']
    invalidECEClasses = [num for num in ECEClassNums if num in INVALID_UPPER_LEVEL_ECE]
    if (len(invalidECEClasses) > 0):
        problems.append(f'The following courses are not acceptable upper-level ECE electives {invalidECEClasses}.')
    
    foundationalCourses = [ class_ for class_ in ECEClassNums if class_ in ECE_FOUNDATION]
    if ( (3030 not in foundationalCourses) and (3150 not in foundationalCourses) ):
        problems.append('You need to take either ECE 3030 or ECE 3150.')
    
    if ( (3100 not in foundationalCourses) and (3250 not in foundationalCourses) ):
        problems.append('You need to take either ECE 3100 or ECE 3250.')
    
    if ( len(foundationalCourses) < 3 ):
        problems.append(f'You need to take at least three ECE foundational courses ({ strFormatter(ECE_FOUNDATION, "ECE") }).')

    # AAE
    requirementData = data.loc[['AAE']]
    classes = [class_.split() for class_ in requirementData.iloc[0] if not pd.isnull(class_)]

    courses = []
    for course in classes:
        courses += [course[0] + ' ' + course[1]]

    if ( len(classes) ):
        problems.append(f'Verify with your advisor that they approve of these courses as AAE: {", ".join(courses)}.')
    else:
        problems.append(f'You have not taken any AAE classes.')

    return problems

def analyzeData(uploadedFile):
    problems = []
    fileData = pd.read_csv(uploadedFile, names = ['Category', 'Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9'], engine = 'python', index_col = 'Category')
    fileData = fileData.iloc[1: , :] # remove the first row
    print('FILE DATA')
    
    print(fileData)
    
    problems += simpleRequirements(fileData)
    problems += complicatedRequirements(fileData)

    # Check LS requirement
    lsData = fileData.loc[['LIBERAL STUDIES']]
    lsClasses = [class_.strip() for class_ in lsData.iloc[0] if not pd.isnull(class_)]
    problems += analyzeLS(lsClasses)

    return fileData, problems

def analyzeLS(classes):
    problems = []
    df = pd.read_csv('liberal_studies.csv')
    
    categories = []
    for class_ in classes:
        categories += [category for category in df[ df['Department + Course Number'] == class_].iloc[:, 0]]
    
    # Remove redundant categories
    categories = np.unique(categories)

    allCategories = LS_REQUIREMENT_SATISFIER.keys()
    possibleLSCourses = []

    for category in allCategories:
        if (category not in categories):
            possibleLSCourses.append( f'These courses: {", ".join(LS_REQUIREMENT_SATISFIER[category])} can be used to satisfy the {category} requirement.' )

    numLSCategories = len(categories)
    if (numLSCategories < NUM_LS_CAT):
        problems.append(f'You have not taken enough LS categories. You have only taken {", ".join(categories)}, but you need {NUM_LS_CAT} categories. ' +
        f'Here are some liberal studies suggestions -  {" ".join(possibleLSCourses)}')

    return problems

def getRequirement(class_):
    reqs = []
    for req in MULTI_OPTION:
        if (class_ in MULTI_OPTION[req]):
            reqs.append(req.lower())
    
    sep_ = class_.split(' ')
    if (sep_[0] == 'ECE' and int(sep_[1]) in ECE_FOUNDATION):
        reqs.append('ECE Foundational')

    if (len(reqs) == 0):
        return NOT_INCORPORATED
    
    return ', '.join(reqs)
