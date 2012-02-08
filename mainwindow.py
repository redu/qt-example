# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Feb  8 12:45:32 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 384)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 381, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.coligado = QtGui.QPushButton(self.centralwidget)
        self.coligado.setGeometry(QtCore.QRect(410, 20, 93, 27))
        self.coligado.setObjectName("coligado")
        self.curso = QtGui.QPushButton(self.centralwidget)
        self.curso.setGeometry(QtCore.QRect(410, 70, 93, 27))
        self.curso.setObjectName("curso")
        self.disciplina = QtGui.QPushButton(self.centralwidget)
        self.disciplina.setGeometry(QtCore.QRect(410, 120, 93, 27))
        self.disciplina.setObjectName("disciplina")
        self.turma = QtGui.QPushButton(self.centralwidget)
        self.turma.setGeometry(QtCore.QRect(410, 170, 93, 27))
        self.turma.setObjectName("turma")
        self.novo = QtGui.QPushButton(self.centralwidget)
        self.novo.setGeometry(QtCore.QRect(140, 320, 93, 27))
        self.novo.setObjectName("novo")
        self.editar = QtGui.QPushButton(self.centralwidget)
        self.editar.setGeometry(QtCore.QRect(250, 320, 93, 27))
        self.editar.setObjectName("editar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.coligado.setText(QtGui.QApplication.translate("MainWindow", "Coligados", None, QtGui.QApplication.UnicodeUTF8))
        self.curso.setText(QtGui.QApplication.translate("MainWindow", "Cursos", None, QtGui.QApplication.UnicodeUTF8))
        self.disciplina.setText(QtGui.QApplication.translate("MainWindow", "Disciplinas", None, QtGui.QApplication.UnicodeUTF8))
        self.turma.setText(QtGui.QApplication.translate("MainWindow", "Turmas", None, QtGui.QApplication.UnicodeUTF8))
        self.novo.setText(QtGui.QApplication.translate("MainWindow", "Novo", None, QtGui.QApplication.UnicodeUTF8))
        self.editar.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))

