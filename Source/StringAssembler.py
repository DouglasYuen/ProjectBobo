## Singleton, one class for creating string outputs from the inputs
## Execution depends on non-null dictionaries for conditions and physical exams
## This is a wrapper that will be called to make the strings 
##
## Version 0.3.0 
## Date 5.26.17

## This class coordinates functionality in the program.
## This design is intended to accommodate the flow where a user picks a condition first before picking a subcondition

## To use this in a different Python script, add: "from StringAssembler import makeStringSetForSubcondition"

## Methods needed by the GUI are:
## makeStringSetForSubcondition to generate a list of all the fields for a sub-condition
## returnAllConditionKeys to get all of the keys for the conditions
## returnAllConditionsForKey to get all of the sub-conditions for a condition (i.e. the key)

# Use this to populate the table

from FileParser import setupDataStructures 

#Strictly for testing, we might need new organisational structure later

listOfPhysicalExams, listOfConditions = setupDataStructures()

# Every key-value pair is a condition-set of subtypes pair
# This method uses the key "condition", which returns a list of subtypes
# From this list, search for the sub-condition, then return all of its fields
# These fields are returned as a string array that can be iterated through
# If nothing is found, this method will return null

def makeStringSetForSubcondition(condition, subcondition, type):
	listOfSubconditions = listOfConditions[condition]
	listOfEntries = []	
	for subtype in listOfSubconditions:
		if subtype.subtypeID == subcondition:
			allFields = subtype.fields
			for field in allFields:
				if field.fieldType == type:
					resultant = makeStringFromFields(field.fieldValue)
					listOfEntries.append(resultant)
#	break

	return listOfEntries

# Determines whether or not a field is a physical exam. If it is, convert it into a string and return it
# If the field is a normal field (i.e. without formatting), return the field as it is found
# This method is flexible, and can be made to look for other starting characters to read from different special types.
# So far, "%" indicates a physical exam, and "$" indicates a tab

#Sam's note: one thing I wanted to do is consoldiate the Physical Exam portions at the end of the "P" progress note .txt file.

CombinedExam=[]#Sam appended
def makeStringFromFields(fieldString):
	firstCharacter = fieldString[0]
	resultant = fieldString
	
	if (firstCharacter == "%"):
		resultant = retrievePhysicalExam(fieldString)
		CombinedExam.append(resultant) #Sam appended
		resultant = "%%%" #Sam appended
	
	
	elif (firstCharacter == "$"):
		resultant = "\t" + fieldString[1:]

	return resultant

# For a field with a physical exam, convert the physical exam ID into a string field 
# If no physical exam is found, it should return null

def retrievePhysicalExam(physicalExamID):
	physicalExamKey = physicalExamID.replace("%", "")
	physicalExamContents = listOfPhysicalExams[physicalExamKey]
	
	return physicalExamContents

# Returns a list of all the keys for the conditions
# Returns an empty list if the conditions are empty
# Call me first! Do this right away!

def returnAllConditionKeys():
	return list(listOfConditions.keys())

# Returns a list of all the conditions for a particular key
# Returns an empty list if there are no values for that key
# Call me when a user clicks on something in the first column!

def returnAllConditionsForKey(keyName):
	return listOfConditions[keyName]
	
# Example usage

#print(makeStringSetForSubcondition("COPD", "COPD Acute Exacerbation", "P"))
#print(makeStringSetForSubcondition("Pneumonia", "Community Acquired Pneumonia", "P"))
