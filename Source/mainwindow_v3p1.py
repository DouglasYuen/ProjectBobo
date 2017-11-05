'''
** RUN THIS FILE **

version 3.1: click print prompts user agreement. Added ui_user_agreement.ui and .py
The window expects Disclaimers.html in the same directory

Version 3:
Main window connecting stuff on the GUI (in ui_mainwindow_3SQ.py) with the program functionality
Uses ColumnView instead of ListViews

Note: runs with Python 3, PyQt5
Reqs: FileParser, StringAssembler (comment out the test lines)

Author: Rose and Samuel

Resources: 
http://nikolak.com/pyqt-qt-designer-getting-started/ **this is in PyQt4
http://zetcode.com/gui/pyqt5/firstprograms/
http://doc.qt.io/qt-5/modelview.html
http://www.binpress.com/tutorial/building-a-text-editor-with-pyqt-part-one/143
https://stackoverflow.com/questions/33924369/how-to-open-a-window-with-a-click-of-a-button-from-another-window-using-pyqt

Sam's Excel-file to-do list:
-Find a way to categorize conditions / subconditions
-Create blank spaces for extra conditions not included in the CSV

Program to-do:
-Set up something to extend __ for typing vs. writing on paper
-Maybe consider moving Print Button function to a different "File Writer" file.

to do:
-implement checkboxes or way of quickly removing added item
-file output options
-restructure to only get subconditions when condition is selected
-format form text
-fix QAccessibleTable::child invalid index errors when...? too many are added?
 (this has to do with accessibility options)

potential problem spots:
-addSelectionsToForm
-there must be a more efficient way to populate the model from the dictionary
-populateModel: there must be a more general way to make the model and make this work
-is it more efficient to just grab the subtypeID or to subclass QStandardItem somehow
 to make populateModel() work with Condition class objects?
'''

import sys    # for passing argv into QApplication
from PyQt5.Qt import *    # still unsure what best to import
from ui_mainwindow_v3 import Ui_MainWindow
from ui_user_agreement import Ui_userAgreement

# the code that generates the lists
from StringAssembler import *

#This is the list that will contain the selected subconditions
FinalList=[]

class DisplayWindow(QMainWindow, Ui_MainWindow):

	def __init__(self):
		super().__init__() #lots of diff ways to set this up?

		self.setupUi(self)
		self.newWindow = None
		
		#default values
		customText = ""

		#populate model and view
		dictOfConditions = self.assembleConditionDictionary()
		self.theDataStructure = self.makeConditionModel()

		# TESTING-------------------
#		testData = {'adc':['cait','kayle'], 'supp':['zyra','janna','nami'], 'you':[]}

#		self.populateModel(self.theDataStructure, testData) # for testing
		customText=" your face"
		#-----------------------------

		self.populateModel(self.theDataStructure, dictOfConditions)
		self.conditionsViewer.setModel(self.theDataStructure) #this needs to be before setting selection model
		self.selectedConditions = self.conditionsViewer.selectionModel() # separate model

		#connect buttons
		self.selectedConditions.selectionChanged.connect(lambda: self.addSelectionsToForm(self.selectedConditions))
		self.printButton.clicked.connect(self.showAgreement)
		self.clearAllButton.clicked.connect(self.MainConditionList.clear)
		self.clearAllButton.clicked.connect(self.SubConditionList.clear)
		self.addButtonCondition.clicked.connect(self.addToMainList)
		self.addButtonSubCondition.clicked.connect(self.addToSubList)
		self.removeButton.clicked.connect(self.removeFromList)


	def showAgreement(self):
	# when the print button is clicked, opens a new window displaying user agreement
	# agree button makes the forms and closes the dialog
	# decline button closes the dialog

		self.newWindow = QMainWindow()
		userAgreement = Ui_userAgreement()
		userAgreement.setupUi(self.newWindow)

		self.uaText = "Disclaimers.html"

		if self.uaText:
			with open(self.uaText) as file:
				userAgreement.textBrowser.setHtml(file.read())

		self.newWindow.show()
		
		#connect buttons
		userAgreement.agreeButton.clicked.connect(self.genFinalList)
		userAgreement.agreeButton.clicked.connect(self.newWindow.close)
		userAgreement.declineButton.clicked.connect(self.newWindow.close)

# -------------------------------------------------------------------------------------------
# Tree Library
# -------------------------------------------------------------------------------------------

	def assembleConditionDictionary(self):
	#initializes the condition dictionary using methods from StringAssembler.py

		conditionKeys = returnAllConditionKeys() #list
		dictionary = {}

		for key in conditionKeys:

			subconditions = returnAllConditionsForKey(key) #list
			sublist = []
			
			for subcondition in subconditions:

				sublist.append(subcondition.subtypeID) #get the str name of the subcondition
			
			dictionary[key] = sublist

		return dictionary


	def makeConditionModel(self):
	# makes the "model" that hosts the lists of conditions and subconditions

		model = QStandardItemModel()

		return model


	def populateModel(self, model, inputDictionary):
	# This method assumes the input is the form {a:[b,c,...],...} where b, c... are 
	# Condition type. A more general way would be to restructure the model so this 
	# method can be recursive?

		for condition, subconditions in inputDictionary.items(): #to loop over dict
			item = QStandardItem(condition)
			model.appendRow(item)

			if subconditions:
				for subcondition in subconditions:
					subitem = QStandardItem(subcondition)
					"""
					# make and append the strings
					stringForSubcondition = makeStringSetForSubcondition(condition, subcondition)
					
					for subsubitem in stringForSubcondition:
						stringItem = QStandardItem(subsubitem)
						subitem.appendRow(stringItem)
					"""
					item.appendRow(subitem)

# -------------------------------------------------------------------------------------------
#BUTTONS
# -------------------------------------------------------------------------------------------

	def addSelectionsToForm(self, selectionModel):
	# when items are selected, add, parse and display in selectionPreview
		#get selected items from conditionsViewer
		self.AlphaBox.clear()
		selectedIndices = selectionModel.selectedIndexes()
			
		for index in selectedIndices:
			
			selectedItem = self.theDataStructure.itemFromIndex(index)
			theString = selectedItem.text()
			
			#display in the QtextEdit box 
			self.AlphaBox.setText(theString)

#Remove button function
	def removeFromList(self):
		for item in self.MainConditionList.selectedItems():
			self.MainConditionList.takeItem(self.MainConditionList.row(item))
		for item in self.SubConditionList.selectedItems():
			self.SubConditionList.takeItem(self.SubConditionList.row(item))

#Add button function
	def addToMainList(self):
		self.MainConditionList.addItem(self.AlphaBox.text())

	def addToSubList(self):
		self.SubConditionList.addItem(self.AlphaBox.text())

# -------------------------------------------------------------------------------------------
# the File Writer
# -------------------------------------------------------------------------------------------
	def genFinalList(self):
	
	
		FinalListMain=([item.text() for item in self.MainConditionList.selectedItems()])
		FinalListSub=([item.text() for item in self.SubConditionList.selectedItems()])
		
		DictOutput = dict(zip(FinalListMain, FinalListSub))
		
		#Creating .txt files
		ProgressFile = open("z.Progress Note.txt","w")
		HandoverFile = open("z.Handover File.txt","w")
		
		count=1
		
		#Format for the Progress Note
		ProgressFile.write("PROGRESS NOTE" + '\n')
		ProgressFile.write("Date:" + '\n' +'\n')
		ProgressFile.write("Summary:_" + '\n' +'\n')
		
		#This loop generates the conditions for handover and progress notes files
		#Progress Note
		for alpha in DictOutput:
			ProgressFile.write(str(count) + ". " + DictOutput[alpha].upper() + '\n')
			Z = makeStringSetForSubcondition(alpha,DictOutput[alpha],"P")
			for beta in Z:
				if (beta == "%%%"):
					ProgressFile.write("")
				else:
					ProgressFile.write(str(beta) + '\n')
			#ProgressFile.write(" ".join(str(x) for x in Z))
			ProgressFile.write('\n')
			ProgressFile.write('\n')
			count=count+1
		count=1
		#Append P/E to Progress Note
		#I am sure there is a better way to shorten to unique entries only in an order that makes sense. But until then...we're stuck with this I guess.
		ProgressFile.write("PHYSICAL EXAM:" + '\n')
		CombinedExamUniqueOnly=[]
		for gamma in CombinedExam:
			if gamma not in CombinedExamUniqueOnly:
				CombinedExamUniqueOnly.append(gamma)
		CombinedExam.clear()
		CombinedExamUniqueOnly.sort()
		for delta in CombinedExamUniqueOnly:
			if int(delta[0:2]) < 50:
				delta=delta[4:]
				if delta[0] == "^":
					ProgressFile.write('\n' + str(delta[1:]) + '\n')
				else:
					ProgressFile.write(str(delta) + '\n')
		ProgressFile.write('\n' + "INVESTIGATIONS:" + '\n')
		for delta in CombinedExamUniqueOnly:
			if int(delta[0:2]) > 50:
				delta=delta[4:]
				if delta[0] == "^":
					ProgressFile.write('\n' + str(delta[1:]) + '\n')
				else:
					ProgressFile.write(str(delta) + '\n')
	
		#Format for Handover file
		HandoverFile.write("THE CHECKLIST" + '\n')
		HandoverFile.write("Date created:" + '\n' +'\n')
		HandoverFile.write("Summary:_" + '\n' +'\n')
		HandoverFile.write("Advanced Care Plan:___" + '\n')
		HandoverFile.write("Patient is from: Home, Senior's Apartment, Assisted Living, SL3, SL4, or LTC" + '\n')
		
		HandoverFile.write('\n'+"TASKS TO BE DONE DAILY:"+'\n')
		HandoverFile.write("Dates:")
		for i in range(18):
			HandoverFile.write(" ")
			i = i + 1
		HandoverFile.write(" || ")
		for i in range(15):
			HandoverFile.write(" ")
			i = i + 1
		HandoverFile.write(" |___|___|___|___|___|___|___|" +'\n')
	
	
		DailyTasks=[]
		HospitalizationTasks=[]
		DischargeTasks=[]
		
		for alpha in DictOutput:
			Y = makeStringSetForSubcondition(alpha,DictOutput[alpha],"H")
			Z = str(DictOutput[alpha])
			Spaces="                         "
			if len(Z) > 25:
				Z=Z[0:24]
			for beta in Y:
				X=str(beta)
				if X[0] != "@":
					if X[0] != "#":
						while len(Z) < 25:
							Z += "_"
						while len(X) < 15:
							X += " "
						if len(X) == 15:
							HandoverFile.write(Z + "|| " + X)
							HandoverFile.write(" |___|___|___|___|___|___|___|" +'\n')
						elif len(X) > 15:
							while len(X) < 57:
								X += " "
							HandoverFile.write(Z + "|| " + X[0:44] + '\n')
							HandoverFile.write(Spaces + "|| " + "    " + X[45:56] +" |___|___|___|___|___|___|___|" +'\n')
			count=count+1

		#Additional Blank Options at the end
		for j in range(3):
			for i in range(25):
				HandoverFile.write("_")
				i = i + 1
			HandoverFile.write("||_")
			for i in range(16):
				HandoverFile.write("_")
				i = i + 1
			HandoverFile.write("|___|___|___|___|___|___|___|" +'\n')
			j=j+1
		HandoverFile.write('\n')
		count=1
		HandoverFile.write('\n'+"TASKS FOR THIS HOSPITAL STAY:"+'\n')
		
		for alpha in DictOutput:
			Y = makeStringSetForSubcondition(alpha,DictOutput[alpha],"H")
			Z = str(DictOutput[alpha])
			if len(Z) > 25:
				Z=Z[0:24]
			for beta in Y:
				X=str(beta)
				if X[0] == "@":
					HandoverFile.write(Z + " || " + X[1:] + '\n')

		HandoverFile.write('\n'+"MEDICAL TASKS FOR DISCHARGE:"+'\n')
		for alpha in DictOutput:
			Y = makeStringSetForSubcondition(alpha,DictOutput[alpha],"H")
			Z = str(DictOutput[alpha])
			if len(Z) > 25:
				Z=Z[0-24]
			for beta in Y:
				X=str(beta)
				if X[0] == "#":
					HandoverFile.write(Z + " || " + X[1:] + '\n')

		HandoverFile.write('\n')
	
		HandoverFile.write('\n'+"ADDITIONAL TASKS REQUIRED ON DISCHARGE:"+'\n')
		HandoverFile.write("Patient's Disposition is: Home, Senior's Apartment, Assisted Living, SL3, SL4, or LTC" + '\n')
		HandoverFile.write("Patient is to be followed up by::"+'\n')
		for i in range(3):
			HandoverFile.write('\t'+"___________________"+'\n')
		HandoverFile.write("Mobility & Function Agreed by PT + OT:___"+'\n')
		HandoverFile.write('\n'+"Problem List:" +'\n')
		for beta in FinalListSub:
			HandoverFile.write(str(count) + ". " + beta + '\n')
			count=count+1
		
		ProgressFile.close()
		HandoverFile.close()

# -------------------------------------------------------------------------------------------
#Some old code attempting to send to a Text Editor Widget
# -------------------------------------------------------------------------------------------

"""
	def saveForm(self):
	# grabs text in text editor and saves to a text file in HTML to preserve style

		with open('finalForm.txt', 'wt') as theFileOutput:

			theFileOutput.write(self.selectionPreview.toHtml())


	def previewForm(self): 
	# shows print preview and option to print to printer

		printPreview = QPrintPreviewDialog()
		printPreview.paintRequested.connect(lambda p: self.selectionPreview.print_(p))
		printPreview.exec_()


	def printForm(self):
		confirm = QPrintDialog()
		
		if confirm.exec_()== QDialog.Accepted:

			self.selectionPreview.print_(confirm.printer())
		
"""


def main():
	app = QApplication(sys.argv)
	form = DisplayWindow()
	form.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
