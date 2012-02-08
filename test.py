#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow

class TestWindow(QtGui.QMainWindow, Ui_MainWindow):
        def __init__(self):
                QtGui.QMainWindow.__init__(self)

                self.setupUi(self)

                self.connect(self.coligado, QtCore.SIGNAL('clicked()'),self.related)


        def related(self):
                self.listWidget.addItem("Coligados tem que aparecer na janela")

app = QtGui.QApplication(sys.argv)
form = TestWindow()
form.show()
app.exec_()
