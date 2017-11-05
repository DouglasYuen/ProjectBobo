## Physical exam class, contains a list of field values associated with a particular physical exam
##

from Field import Field

class PhysicalExam():
	
	def __init__(self, theExamName, theField):
		self.examName = theExamName
		self.examField = theField
	
	def modifyField(self, theFieldID):
		newField = Field(theFieldID)
		self.listOfFields.append(newField)