## Condition class, holding onto a list of attributes
## Dated

from Field import Field

class Condition():
	
	#Initialiser method
	
	def __init__(self, theCondition, theSubtype):
		self.conditionID = theCondition
		self.subtypeID = theSubtype
		self.fields = []
		
	def addFieldToCondition(self, theField):
		self.fields.append(theField)