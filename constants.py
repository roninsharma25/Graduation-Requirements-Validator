# Total number of required classes
NUM_FWS = 2
NUM_PE = 2
NUM_ENGRI = 1
NUM_ENGRD = 1
NUM_CDE = 1

# Total number of required credits
NUM_LS_CREDITS = 18

# Total number of required categories
NUM_LS_CAT = 3

# Classes satisfying core requirements
CORE_CLASSES = {
    'Math': [1910, 1920, 2930, 2940],
    'Physics': [1112, 2213, 2214],
    'Chemistry': [2090],
    'CS': [1110]
}

# Minimum number Requirements
MIN_NUMBER = {
    'PE': 2,
    'FWS': 2,
    'ENGRI': 1,
    'ENGRD': 1,
    'LIBERAL STUDIES': 6,
    'CDE': 1
}

# Class-specific Requirements
CLASS_SPECIFIC = {
    'CORE MATH': [1910, 1920, 2930, 2940],
    'CORE PHYSICS': [1110, 1112, 2213, 2214],
    'CORE CHEMISTRY': [2090],
    'CORE CS': [1110],
    'CORE ECE': [2100, 2300, 2720],
}

MULTI_OPTION = {
    'PROBABILITY': ['ENGRD 2700', 'ECE 3100'],
    'ADVANCED COMPUTING': ['CS 2110', 'ECE 2400', 
        'ENGRD 3200', 'AEP 4380', 'ECE 4740',
        'ECE 4750', 'ECE 4760'],
    'CDE': [4370, 4530, 4670, 4740, 4750, 4760],
    'TECHNICAL WRITING': ['ENGRC 3023', 'ENGRC 3350', 
        'ENGRC 3500', 'ECE 4760']
}
