#-----------------------------------------------------------------------------#
# Title: Soc.py
# Desc: Script demonstrating SoC concept, based on Basic_Math.py (Assginment02)
# Change Log: (Who, When, What)
# DBiesigner, 2030-Jan-01, Created File
# Tiago, 2022-Nov-12, Modified to demonstrate SoC
# Tiago, 2022-Nov-12, Modified to demonstrate Functions
#-----------------------------------------------------------------------------#

# -- DATA -- #
intNumA = None
intNumB = None
intSum = None
intDif = None
intPro = None
intQuo = None

# -- PROCESSING -- #
# Process the data
def getSum():
    return intNumA + intNumB

def getDif():
    return intNumA - intNumB

def getPro():
    return intNumA * intNumB

def getQuo():
    return intNumA / intNumB

# -- PRESENTATION (Input/Output -- #
# Get user input data
print('Basic Math script. Calculating the Sum, Difference, Product and Quotient of the numbers.')
intNumA = int(input('Please enter the 1st number: '))
intNumB = int(input('Please enter the 2st number: '))
# Display the Results
print('\n\nThis script calculated using the Numbers', intNumA, 'and', intNumB)
print('The Results are:\n')
print('Sum:\t\t', getSum(), '\nDifference:\t', getDif())
print('Product:\t', getPro(), '\nQuotient:\t', getQuo())
