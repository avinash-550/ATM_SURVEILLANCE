import sys,time,os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from contextlib import contextmanager
import math
from ui import Ui_MainWindow

danger = 0

class WorkerThread(QtCore.QThread):

	##signal##
	signal = QtCore.pyqtSignal(list,name="signal1")

	def __init__(self,parent=None):
		super(WorkerThread, self).__init__(parent)

	def run(self):
		global danger

		danger = 1

		self.signal.emit([danger])

class mainProgram(QtWidgets.QMainWindow,Ui_MainWindow):
	signal = QtCore.pyqtSignal(str)

