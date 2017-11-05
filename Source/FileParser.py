## Singleton, one class for parsing files into the program
## Once the CSV files are parsed, we create two arrays that can be accessed from anywhere
## 
## Version 0.1.0, 
## Date 3.29.17

from Field import Field
from PhysicalExam import PhysicalExam
from Condition import Condition

import csv

listOfConditions = {}
listOfPhysicalExams = {}
listOfChecklistItems = {}

# Constants for Physical Exams

PHYSICAL_COLUMN = 0
PHYSICAL_LINE_COLUMN = 1
TEXT_COLUMN = 2

# Constants for Conditions

CONDITION_COLUMN = 0
SUBTYPE_COLUMN = 1
PROGRESS_COLUMN = 2
LINE_NUMBER_COLUMN = 3
FIELD_COLUMN = 4

# Read through the CSV file containing the physical exams and create the list of exams

def populateListOfPhysicalExams(theFileName):
	with open(theFileName, 'r') as csvfile:
		fileReader = csv.reader(csvfile)
		next(fileReader)
		for row in fileReader:
			makePhysicalExam(row[PHYSICAL_COLUMN], row[PHYSICAL_LINE_COLUMN], row[TEXT_COLUMN])

# Read through the CSV file containing the checklist items and create the list of checklist items
# Checklist items are simplified versions of the fields that can be quickly checked off

def populateListOfChecklistItems(theFileName):
	print("Test")
			
# Read through the CSV file containing the conditions and make the list of conditions
# Only call this after physical exams are generated!

#Create a dictionary with key condition and value list of subtypes
#For each condition, create a new subtype as an object when that is encountered
#While the subtype has not changed, add the field to that subtype

# The first item in the csv is a condition identifier, and the second column contains the condition itself

def populateListOfConditions(theFileName):
	with open(theFileName, 'r', encoding='mac_roman') as csvfile:
		fileReader = csv.reader(csvfile)		
		next(fileReader)
		previousRowID = ""
		previousRowCondition = ""
		for row in fileReader:
			if row[CONDITION_COLUMN] == "" or row[CONDITION_COLUMN] != previousRowID:
				listOfConditions[row[CONDITION_COLUMN]] = []
				newCondition = Condition(row[CONDITION_COLUMN], row[SUBTYPE_COLUMN])
				newField = Field(row[SUBTYPE_COLUMN], row[LINE_NUMBER_COLUMN], row[FIELD_COLUMN], row[PROGRESS_COLUMN])
				newCondition.addFieldToCondition(newField)
				listOfConditions[row[CONDITION_COLUMN]].append(newCondition)
			elif row[CONDITION_COLUMN] == previousRowID:
				if row[SUBTYPE_COLUMN] == previousRowCondition:
					newField = Field(row[SUBTYPE_COLUMN], row[LINE_NUMBER_COLUMN], row[FIELD_COLUMN], row[PROGRESS_COLUMN])
					conditionReference = listOfConditions[row[CONDITION_COLUMN]]
					conditionReference[-1].addFieldToCondition(newField)
				elif row[SUBTYPE_COLUMN] != previousRowCondition:
					newCondition = Condition(row[CONDITION_COLUMN], row[SUBTYPE_COLUMN])
					newField = Field(row[SUBTYPE_COLUMN], row[LINE_NUMBER_COLUMN], row[FIELD_COLUMN], row[PROGRESS_COLUMN])
					newCondition.addFieldToCondition(newField)
					listOfConditions[row[CONDITION_COLUMN]].append(newCondition)
			previousRowID = row[CONDITION_COLUMN]
			previousRowCondition = row[SUBTYPE_COLUMN]
#			lastConditionID = row[0]

# Creates a new field for that condition and returns the field

def makeFieldForCondition(fieldID, fieldOrder):
	theField = Field(fieldID, fieldOrder)
	return theField

# From the data read in, makes an object containing the condition and returns the condition

def makeCondition(theID, theSubtype, theProgressType):
	theCondition = Condition(theID, theSubtype, theProgressType)
	return theCondition

# Need a method to add fields to the appropriate condition!
# From the data read in, makes an object containing the physical exam and adds it to the list of all exams
	
def makePhysicalExam(theID, row, value):
	examID = theID + row
	#examInstance = PhysicalExam(examID, value)
	listOfPhysicalExams[examID] = value

# Makes the simple checklist for a given condition
#
	
# Formats the physical exams so that the parsing notation is removed.
# The method does an in-place clean-up, acting on the instance variable.
	
def cleanPhysicalExams():
	listOfPhysicalExamKeys = list(listOfPhysicalExams.keys())
	listOfPhysicalExamKeys.sort()

	for i in range(0, len(listOfPhysicalExamKeys)):
		
		if (i < len(listOfPhysicalExamKeys) - 1):
			currentKey = listOfPhysicalExamKeys[i]
			nextKey = listOfPhysicalExamKeys[i+1]
			
			formattedCurrentKey = currentKey[:-1]
			formattedNextKey = nextKey[:-1]

			if((formattedCurrentKey != formattedNextKey) and (currentKey.endswith("1"))):
				listOfPhysicalExams[formattedCurrentKey] = listOfPhysicalExams.pop(currentKey)
			
		elif (i == len(listOfPhysicalExamKeys) - 1):
			currentKey = listOfPhysicalExamKeys[i]
			formattedCurrentKey = currentKey[:-1]
			
			if(currentKey.endswith("1")):
				listOfPhysicalExams[formattedCurrentKey] = listOfPhysicalExams.pop(currentKey)

# Method for checking the first character of the parameter, theField, passed in, compared to a character of choice
# Returns true if the characters match, returns false otherwise

def checkFirstCharacter(theField, character):
	if (theField[:1] == character):
		return True
	else:
		return False

# Function for setting things up. Only this should be called from external classes

def setupDataStructures():
	populateListOfPhysicalExams('PhysicalExam.csv')
	populateListOfConditions('Conditions.csv')
	cleanPhysicalExams()
	
	# Add the checklist contents here
	
	#print(listOfConditions)
	return listOfPhysicalExams, listOfConditions

