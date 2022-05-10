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

# All requirements
ALL_REQUIREMENTS = ['PE', 'FWS', 'ENGRI', 'CORE MATH', 'CORE PHYSICS',
                    'CORE CHEMISTRY', 'CORE CS', 'CORE ECE', 'LIBERAL STUDIES',
                    'ENGRD', 'UPPER LEVEL', 'OTE', 'AAE', 'PROBABILITY',
                    'ADVANCED COMPUTING', 'CDE', 'TECHNICAL WRITING']

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
    'CORE PHYSICS': [1112, 2213, 2214],
    'CORE CHEMISTRY': [2090],
    'CORE CS': [1110],
    'CORE ECE': [2100, 2200, 2300],
}

MULTI_OPTION = {
    'PROBABILITY': ['ENGRD 2700', 'ECE 3100'],
    'ADVANCED COMPUTING': ['CS 2110', 'ECE 2400', 
        'ENGRD 3200', 'AEP 4380', 'ECE 4740',
        'ECE 4750', 'ECE 4760'],
    'CDE': ['ECE 4370', 'ECE 4530', 'ECE 4670', 'ECE 4740', 'ECE 4750', 'ECE 4760'],
    'TECHNICAL WRITING': ['ENGRC 3020', 'ENGRC 3023', 'ENGRC 3025', 'ENGRC 3111', 
                          'ENGRC 3120', 'ENGRC 3152', 'ENGRC 3340', 'ENGRC 3350',
                          'ENGRC 3500', 'ENGRC 3610', 'ENGRC 3640', 'ENGRC 4152',
                          'ENGRC 4590']
}

INVALID_UPPER_LEVEL_ECE = [3600, 4999, 5830, 5870, 5880]
ECE_FOUNDATION = [3030, 3100, 3140, 3150, 3250]

REQUIREMENT_MAPPER = {
    'CORE MATH': 'MATH',
    'CORE PHYSICS': 'PHYS',
    'CORE CHEMISTRY': 'CHEM',
    'CORE CS': 'CS',
    'CORE ECE': 'ECE'
}

LS_REQUIREMENT_SATISFIER = {
    'CA': ['AAS 1100', 'AEM 4421', 'AIIS 1110', 'AMST 1101', 'ANTHR 1190'],
    'HA': ['AAS 2042', 'AIIS 1110', 'AMST 1540', 'ANTHR 1200', 'ARTH 2200'],
    'KCM': ['AEM 2020', 'AIIS 2100', 'AMST 3121', 'ANTHR 4101', 'ARAB 4867'],
    'LA': ['AAS 2620', 'AIIS 2600', 'AKKAD 1411', 'AMST 1312', 'ANTHR 3110'],
    'SBA': ['AAS 3400', 'AEM 1300', 'AIIS 2240', 'AMST 1104', 'ANTHR 2400'],
    'CE': ['ENGRC 3023', 'ENGRC 3350', 'ENGRC 3500']
}

NOT_INCORPORATED = "That class hasn't been incorporated into the dataset yet."