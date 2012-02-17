#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from main_window import Ui_MainWindow
import urlRequest       

class APIWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.setupUi(self)
        
        self.connect(self.enviroment, QtCore.SIGNAL('clicked()'),self.related)
        self.connect(self.course, QtCore.SIGNAL('clicked()'),self.course_related)
        self.connect(self.disciplina, QtCore.SIGNAL('clicked()'),self.discipline_related)
#        self.connect(self.turma, QtCore.SIGNAL('clicked()'),self.gang)
#        self.connect(self.novo, QtCore.SIGNAL('clicked()'),self.new)
#        self.connect(self.editar, QtCore.SIGNAL('clicked()'),self.update)
      
    def related(self):
        self.listWidget.clear()
        content = urlRequest.listRelated
        for iterate in content:
            self.listWidget.addItem(iterate['name'])
    def course_related(self):
        self.listWidget.clear()
        content = urlRequest.listRelated
        for iterate in content:
                        self.comboBox.addItem(iterate['name'])
                        
        self.comboBox.activated[str].connect(self.onActivated)

    def discipline_related(self):
        self.listWidget.clear()
        
    def onActivated(self, text):
        self.listWidget.clear()
        courses = urlRequest.get_courses(text)
        for iterate in courses:
            self.listWidget.addItem(iterate['name'])


        


      
      
app = QtGui.QApplication(sys.argv)
form = APIWindow()
form.show()
app.exec_()
