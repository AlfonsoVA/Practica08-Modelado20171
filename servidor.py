# -*- coding: utf-8 -*-
 
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
 
clase = uic.loadUiType("servidor.ui")[0]

class Servidor(QtGui.QMainWindow, clase): 	
	
 def __init__(self):  
 	QtGui.QMainWindow.__init__(self)  
 	self.setupUi(self)
 	self.tableWidget.horizontalHeader().setResizeMode(QHeaderView.Stretch)
 	self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) 
 	self.tableWidget.verticalHeader().setResizeMode(QHeaderView.Stretch)  
 	self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) 



app= QtGui.QApplication(sys.argv)
Ventana= Servidor()
Ventana.show()
app.exec_()