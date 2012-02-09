#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
import urlRequest

def list_related():
        listOut = urlRequest.listRelated
        return listOut
        
class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.lbl = QtGui.QLabel("", self)
        combo = QtGui.QComboBox(self)
        for x in urlRequest.listRelated:
                combo.addItem(x)


        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QtGui.QComboBox')
        self.show()
        
    def onActivated(self, text):
        cursos = urlRequest.get_courses(text)
        TestWindow.joga(form, cursos[0]['name'])
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
                content = list_related()
                for x in content:
                        self.listWidget.addItem(x)

        def course(self):
                self.listWidget.clear()
                combo = Example()
                combo.main()
                self.listWidget.clear()
                
                
        def discipline(self):
                self.listWidget.clear()
                self.listWidget.addItem("Json das disciplinas")
                
        def gang(self):
                self.listWidget.clear()
                self.listWidget.addItem("Gangs")
        
        def new(self):
                self.listWidget.clear()
                self.listWidget.addItem("Criar metodo Novo, nova tela")
                
        def update(self):
                self.listWidget.clear()
                self.listWidget.addItem("criar metodo update")
                
        def joga(self, text):
            self.listWidget.addItem(text)
                
                
app = QtGui.QApplication(sys.argv)
form = TestWindow()
form.show()
app.exec_()
