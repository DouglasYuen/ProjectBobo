'''

Collects each user selected Condition
for the purpose of writing the final text form

Output: form.txt
Requires: Field.py, PhysicalExam.py, Condition.py

Methods wish list:
  -read in values from input and create/append to FileWriter object
  -format and print each Condition in FileWriter to text file

Project: SURGEON aka Project Douglas, a tool to cut 
down Sam's paperwork. Poor Sam.

Author: Rose

'''
from datetime import datetime

from Field import Field
from PhysicalExam import PhysicalExam
from Condition import Condition

class FileWriter:
	# The form into which the list of Conditions is plugged

	# Initialiser method
	def __init__(self):
		self.listOfConditions=[]
		self.theDate = datetime.today()
		self.getDate = self.theDate.strftime("%H:%M %d-%b-%Y")
		self.preamble = self.getDate+"\n\n"+"Patient info:\n"

	# Edit preamble for entering patient info from interface
	def addToPreamble(self,addedText):
		self.preamble += (addedText+"\n")  #added \n
		return self.preamble

	# append a new Condition
	def addCondition(self,theCondition):
		if isinstance(theCondition,Condition):
			self.listOfConditions.append(theCondition)
			print "Condition added"
		else:
			print "That is not a Condition"

	# remove a Condition
	def delCondition(self, theCondition):
		if isinstance(theCondition,Condition):
			try:
				self.listOfConditions.remove(theCondition)
				print "Condition deleted"
			except ValueError:
				print "Could not find Condition to delete"
		else:
			print "That is not a Condition"

	# append a new Physical Exam

	# append a new Field

	# print to file (rudimentary)
	def makeForm(self, textFile="form.txt"):
		target = open(textFile, 'w')
		target.write(self.preamble)

#		# Writes all the attributes of the Conditions
#		# added by the User to the text file
		target.write("Condition: \n")
		for eachCondition in self.listOfConditions:
			target.write(eachCondition.conditionID)
			target.write("\n")

			target.write("\tSubtypes: \n")

#			for eachSubtype in eachCondition.subtypeID:
#				target.write("\t")
#				target.write(eachSubtype)
#				target.write("\n")

			target.write("\t ")
			target.write(eachCondition.subtypeID)
			target.write("\n")

		target.close()

'''
======================== testing ===========================
'''
a=FileWriter()
a.addToPreamble("Jane Doe")
b=Condition("Pneumonia","bad")
c=Condition("your mom","your face")

a.addCondition(b)
print a.listOfConditions
a.addCondition(c)
print a.listOfConditions
a.delCondition(b)
print a.listOfConditions
a.delCondition(b)

a.addCondition(123)
a.delCondition(123)
a.makeForm()
