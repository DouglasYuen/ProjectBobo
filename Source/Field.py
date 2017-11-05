## Field class, contains two variables for the ID and its corresponding value
##

class Field():
	
	# Initialiser method

	def __init__(self, theIDValue, theOrder, theFieldValue, theFieldType):
		self.fieldID = theIDValue
		self.fieldOrder = theOrder
		self.fieldValue = theFieldValue
		self.fieldType = theFieldType
		
	# Call this to change the custom text of a field
	
	def modifyFieldValue(self, inputValue):
		self.fieldValue = inputValue
		