# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from pymongo_client import conn
from PyQt5 import QtCore, QtGui, QtWidgets
from twilio.rest import Client
from PyQt5.QtWidgets import QMessageBox,QDialog,QPushButton
from PyQt5.QtCore import Qt
import numpy as np 
import cv2 
import imutils 
import datetime 
from gun import va


#TWILIO_PHONE_NUMBER = " +12673802780"
TWILIO_PHONE_NUMBER = " +19472825938" 

DIAL_NUMBERS = ["+916282545709"]


TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"


#client = Client("AC00d044ca066af4a16ee9b3d296846ca1", "89c56a412a4b18591d4e6ebbffda08db")
client = Client("AC660496e4caad6cc5a25f4c04e5acf4f6", "b4c9e2a66a2586c223eeeda2f96b2df6")
danger = 1 


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(478, 636)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(0, 0, 481, 641))
		self.tabWidget.setStyleSheet("\n"
"\n"
"font: 75 8pt \"Sitka Subheading\";")
		self.tabWidget.setObjectName("tabWidget")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.frame = QtWidgets.QFrame(self.tab)
		self.frame.setGeometry(QtCore.QRect(0, 0, 491, 251))
		self.frame.setStyleSheet("background-color:rgb(255, 255, 127)")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.label = QtWidgets.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(210, 30, 71, 31))
		self.label.setStyleSheet("color: rgb(0, 0, 0);")
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.frame)
		self.label_2.setGeometry(QtCore.QRect(80, 80, 321, 141))
		self.label_2.setText("")
		self.label_2.setPixmap(QtGui.QPixmap("../s.jpg"))
		self.label_2.setObjectName("label_2")
		self.frame_2 = QtWidgets.QFrame(self.tab)
		self.frame_2.setGeometry(QtCore.QRect(0, 250, 481, 91))
		self.frame_2.setStyleSheet("background-color:rgb(0, 0, 0)")
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_2.setGeometry(QtCore.QRect(330, 20, 121, 51))
		self.pushButton_2.setStyleSheet("background-color:white;\n"
"border: 7px solid green;\n"
"color:green;\n"
"font-weight:bold;")
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_6.setGeometry(QtCore.QRect(70, 20, 121, 51))
		self.pushButton_6.setStyleSheet("background-color:white;\n"
"border: 7px solid red;\n"
"color:red;\n"
"font-weight:bold;")
		self.pushButton_6.setObjectName("pushButton_6")
		self.frame_3 = QtWidgets.QFrame(self.tab)
		self.frame_3.setGeometry(QtCore.QRect(0, 340, 481, 291))
		self.frame_3.setStyleSheet("background-color: rgb(170, 255, 255);")
		self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
		self.pushButton_3.setGeometry(QtCore.QRect(90, 200, 331, 31))
		self.pushButton_3.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"font: 75 12pt \"Calibri\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
		self.pushButton_3.setObjectName("pushButton_3")
		self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
		self.pushButton_4.setGeometry(QtCore.QRect(150, 40, 201, 51))
		self.pushButton_4.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 75 12pt \"Calibri\";\n"
"font: 75 12pt \"Calibri\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
		self.pushButton_4.setObjectName("pushButton_4")
		self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
		self.pushButton_5.setGeometry(QtCore.QRect(150, 120, 201, 51))
		self.pushButton_5.setStyleSheet("background-color:rgb(85, 85, 255);\n"
"font: 75 12pt \"Calibri\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
		self.pushButton_5.setObjectName("pushButton_5")
		self.tabWidget.addTab(self.tab, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.frame_5 = QtWidgets.QFrame(self.tab_2)
		self.frame_5.setGeometry(QtCore.QRect(-10, 0, 491, 641))
		self.frame_5.setStyleSheet("background-color: rgb(255, 255, 127);")
		self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_5.setObjectName("frame_5")
		self.frame_6 = QtWidgets.QFrame(self.frame_5)
		self.frame_6.setGeometry(QtCore.QRect(10, 0, 481, 80))
		self.frame_6.setStyleSheet("background-color: rgb(170, 255, 255);")
		self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_6.setObjectName("frame_6")
		self.label_4 = QtWidgets.QLabel(self.frame_6)
		self.label_4.setGeometry(QtCore.QRect(160, 30, 191, 31))
		self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.frame_5) 
		self.label_5.setGeometry(QtCore.QRect(10, 90, 231, 31))
		self.label_5.setObjectName("label_5")
		self.formGroupBox = QtWidgets.QGroupBox(self.frame_5)
		self.formGroupBox.setGeometry(QtCore.QRect(10, 140, 231, 221))
		self.formGroupBox.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border: 3px solid grey;")
		self.formGroupBox.setObjectName("formGroupBox")
		self.pushButton = QtWidgets.QPushButton(self.formGroupBox)
		self.pushButton.setGeometry(QtCore.QRect(30, 20, 181, 31))
		self.pushButton.setStyleSheet("border: 3px solid blue;\n"
"background-color: white;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"color: rgb(0, 0, 0);")
		#here
		self.pushButton.setStyleSheet("QPushButton {border: 3px solid blue;\n"
"background-color: white;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"color: rgb(0, 0, 0);}"
			"QPushButton::hover"
                             "{"
                             "background-color : lightgreen;"
                             "}")
		#here
		self.pushButton.setObjectName("pushButton")
		self.pushButton_7 = QtWidgets.QPushButton(self.formGroupBox)
		self.pushButton_7.setGeometry(QtCore.QRect(30, 60, 181, 31))
		self.pushButton_7.setStyleSheet("border: 3px solid blue;\n"
"background-color: white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(0, 0, 0);")
		self.pushButton_7.setObjectName("pushButton_7")
		self.pushButton_8 = QtWidgets.QPushButton(self.formGroupBox)
		self.pushButton_8.setGeometry(QtCore.QRect(30, 100, 181, 31))
		self.pushButton_8.setStyleSheet("border: 3px solid blue;\n"
"background-color: white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(0, 0, 0);")
		self.pushButton_8.setObjectName("pushButton_8")
		self.pushButton_9 = QtWidgets.QPushButton(self.formGroupBox)
		self.pushButton_9.setGeometry(QtCore.QRect(30, 150, 181, 31))
		self.pushButton_9.setStyleSheet("border: 3px solid blue;\n"
"background-color: white;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(0, 0, 0);")
		self.pushButton_9.setObjectName("pushButton_9")
		self.pushButton_10 = QtWidgets.QPushButton(self.frame_5)
		self.pushButton_10.setGeometry(QtCore.QRect(140, 440, 191, 41))
		self.pushButton_10.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"font: 75 12pt \"Calibri\";\n"
"font-weight:bold;\n"
"color: rgb(0, 0, 0);")
		self.pushButton_10.setObjectName("pushButton_10")
		self.tabWidget.addTab(self.tab_2, "")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(1)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">SAFE</span></p></body></html>"))
		self.pushButton_2.setText(_translate("MainWindow", "True Alert"))
		self.pushButton_6.setText(_translate("MainWindow", "False Alert"))
		self.pushButton_3.setText(_translate("MainWindow", "REPORT"))
		self.pushButton_4.setText(_translate("MainWindow", "SOS"))
		self.pushButton_5.setText(_translate("MainWindow", "CHECK VIDEO"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
		self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">SECURITY AIDER</span></p></body></html>"))
		self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#ff0000;\">EMERGENCY SERVICES</span></p></body></html>"))
		self.pushButton.setText(_translate("MainWindow", "CALL POLICE"))
		self.pushButton_7.setText(_translate("MainWindow", "CALL HOSPITAL"))
		self.pushButton_8.setText(_translate("MainWindow", "CALL FIRE DEPARTMENT"))
		self.pushButton_9.setText(_translate("MainWindow", "CALL LOCAL SECURITY"))
		self.pushButton_10.setText(_translate("MainWindow", "HELP"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.setupUi(self)
		self.pushButton_5.clicked.connect(self.video)		# Check Video
		self.pushButton_4.clicked.connect(self.next_slot) # SOS button
		self.pushButton.clicked.connect(self.call_police) # Call Police



	def dial_numbers(self,numbers_list):
		
		global TWILIO_PHONE_NUMBER,TWIML_INSTRUCTIONS_URL,client
		"""Dials one or more phone numbers from a Twilio phone number."""
		con = conn()
		user_col, _ = con.get_conn("atm_centers")
		query = {"address" : "500100"}
		updated = {"$set": {"status": "threat alert!!"}}
		temp = user_col.update_many(query, updated)
		print("database updated!!")
		for number in numbers_list:
			print("Dialing " + number)
			# set the method to "GET" from default POST because Amazon S3 only
			# serves GET requests on files. Typically POST would be used for apps
			client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
								url=TWIML_INSTRUCTIONS_URL, method="GET")

	@QtCore.pyqtSlot()
	def video(self):
		print("Analysing Security Feed")
		va()
		if(danger==1):
			print("Weapon Detected!!")

	def next_slot(self):
		
		print("Page Swithcing -- To Call Interface")

		# Swithcing to Next(Calling) Tab
		self.tabWidget.setCurrentIndex(1)

	def call_police(self):
		global DIAL_NUMBERS
		print("*****")
		
		# Dialog for confrimation 
		
		d = QDialog()
		b1 = QPushButton("ok",d)
		b1.move(50,50)
		d.setWindowTitle("ALERT")
		d.setWindowModality(Qt.ApplicationModal)
		b1.clicked.connect(d.close)
		d.exec_()

		self.dial_numbers(DIAL_NUMBERS)

	def call_securiy(self):
		global DIAL_NUMBERS
		print("*****")
		
		# Dialog for confrimation 
		
		d = QDialog()
		b1 = QPushButton("ok",d)
		b1.move(50,50)
		d.setWindowTitle("ALERT")
		d.setWindowModality(Qt.ApplicationModal)
		b1.clicked.connect(d.close)
		d.exec_()

		self.dial_numbers(DIAL_NUMBERS)
	
	def call_fire(self):
		global DIAL_NUMBERS
		print("*****")
		
		# Dialog for confrimation 
		
		d = QDialog()
		b1 = QPushButton("ok",d)
		b1.move(50,50)
		d.setWindowTitle("ALERT")
		d.setWindowModality(Qt.ApplicationModal)
		b1.clicked.connect(d.close)
		d.exec_()

		self.dial_numbers(DIAL_NUMBERS)
	
	def call_hospital(self):
		global DIAL_NUMBERS
		print("*****")
		
		# Dialog for confrimation 
		
		d = QDialog()
		b1 = QPushButton("ok",d)
		b1.move(50,50)
		d.setWindowTitle("ALERT")
		d.setWindowModality(Qt.ApplicationModal)
		b1.clicked.connect(d.close)
		d.exec_()

		self.dial_numbers(DIAL_NUMBERS)




if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	# MainWindow = QtWidgets.QMainWindow()
	# ui = Ui_MainWindow()
	# ui.setupUi(MainWindow)
	# MainWindow.show()
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())
