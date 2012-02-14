#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
import urlRequest       
import ui_form

class Courses(QtGui.QWidget):
    def __init__(self):
        super(Courses, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.lbl = QtGui.QLabel("", self)
        combo = QtGui.QComboBox(self)
        for iterate in urlRequest.listRelated:
                combo.addItem(iterate)

        combo.move(50, 50)
        self.lbl.move(50, 100)
        combo.activated[str].connect(self.onActivated)
        self.setGeometry(200, 200, 200, 100)
        self.setWindowTitle('QtGui.QComboBox')
        self.setWindowTitle('Cursos')
        self.show()
        
    def onActivated(self, text):
        cursos = urlRequest.get_courses(text)                
        TestWindow.joga(form, cursos)
        self.lbl.setText(text)
        self.lbl.adjustSize()

class Discipline(QtGui.QWidget):
    def __init__(self):
        super(Discipline, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.lbl = QtGui.QLabel("", self)
        combo = QtGui.QComboBox(self)

        for iterate in urlRequest.result:
                combo.addItem(iterate['name'])

        combo.move(50, 50)
        self.lbl.move(50, 100)
        combo.activated[str].connect(self.onActivated)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('QtGui.QComboBox')
        self.setWindowTitle('Disciplinas')    
        self.show()
        
    def onActivated(self, text):
        cursos = urlRequest.get_spaces(text)
        TestWindow.joga(form, cursos)
        self.lbl.setText(text)
        self.lbl.adjustSize()
        
class TestWindow(QtGui.QMainWindow, Ui_MainWindow):
        def __init__(self):
                QtGui.QMainWindow.__init__(self)

                self.setupUi(self)

                self.connect(self.coligado, QtCore.SIGNAL('clicked()'),self.related)
                self.connect(self.curso, QtCore.SIGNAL('clicked()'),self.course)
                self.connect(self.disciplina, QtCore.SIGNAL('clicked()'),self.discipline)
                self.connect(self.turma, QtCore.SIGNAL('clicked()'),self.gang)
                self.connect(self.novo, QtCore.SIGNAL('clicked()'),self.new)
                self.connect(self.editar, QtCore.SIGNAL('clicked()'),self.update)

        def related(self):
                self.listWidget.clear()
                content = urlRequest.listRelated
                for iterate in content:
                        self.listWidget.addItem(iterate)

        def course(self):
                self.listWidget.clear()
                combo = Courses()
                combo.main()
                self.listWidget.clear()
                
        def discipline(self):
                self.listWidget.clear()
                combo = Discipline()
                combo.main()
                self.listWidget.clear()
                
        def gang(self):
                self.listWidget.clear()
                self.listWidget.addItem("Gangs")
        
        def new(self):
                self.listWidget.clear()
                self.listWidget.addItem("Criar metodo Novo, nova tela")
                
        def update(self):
                self.listWidget.clear()
                self.listWidget.addItem("criar metodo update")
                
        def joga(self, listaX):
                self.listWidget.clear()
                global lista
                lista = listaX
                for iterate in listaX:
                    self.listWidget.addItem(iterate['name'])
        
app = QtGui.QApplication(sys.argv)
form = TestWindow()
form.show()
app.exec_()
