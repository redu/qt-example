#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow

def f():
        import urllib
#        full = urllib.urlopen("http://localhost:3000/posts.json")#"https://www.googleapis.com/plus/v1/people/104180219523854245733.json")
#        contents = full.read()
#        return contents
        url = 'http://localhost:3000/posts.json'
        f = urllib.urlopen(url)
        d = f.read()
        return d

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
        
                e = f()
                self.listWidget.addItem(e)

        def course(self):
                self.listWidget.addItem("Curso")
                
        def discipline(self):
                self.listWidget.addItem("Json das disciplinas")
                
        def gang(self):
                self.listWidget.addItem("Gangs")
        
        def new(self):
                self.listWidget.addItem("Criar metodo Novo, nova tela")
                
        def update(self):
                self.listWidget.addItem("criar metodo update")
                
app = QtGui.QApplication(sys.argv)
form = TestWindow()
form.show()
app.exec_()
