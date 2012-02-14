# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form.ui'
#
# Created: Fri Feb 10 15:28:50 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
import urlRequest

class Combo(QtGui.QWidget):
    def __init__(self):
        super(Combo, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        self.lbl = QtGui.QLabel("", self)
        combo = QtGui.QComboBox(self)

        combo.addItem("Coligado")
        combo.addItem("Curso")
        combo.addItem("Disciplina")
        combo.addItem("Turma")


        combo.move(50, 50)
        self.lbl.move(50, 100)
        combo.activated[str].connect(self.onActivated)
        self.setGeometry(200, 200, 200, 100)
        self.setWindowTitle('QtGui.QComboBox')
        self.setWindowTitle('Novo')
        self.show()
        
    def onActivated(self, text):
#        if text == 'Coligado':
#              form = ui_form.Ui_Form()
              
        self.lbl.setText(text)
        self.lbl.adjustSize()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(533, 364)
        self.formLayoutWidget = QtGui.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 531, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.Enviroment = QtGui.QLabel(self.formLayoutWidget)
        self.Enviroment.setObjectName("Enviroment")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.Enviroment)

        self.name_enviroment = QtGui.QLineEdit(self.formLayoutWidget)
        self.name_enviroment.setObjectName("name_enviroment")

        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.name_enviroment)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.path_enviroment = QtGui.QLineEdit(self.formLayoutWidget)
        self.path_enviroment.setObjectName("path_enviroment")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.path_enviroment)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.initials_enviroment = QtGui.QLineEdit(self.formLayoutWidget)
        self.initials_enviroment.setObjectName("initials_enviroment")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.initials_enviroment)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.description_enviroment = QtGui.QTextEdit(self.formLayoutWidget)
        self.description_enviroment.setObjectName("description_enviroment")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.description_enviroment)
        self.submit = QtGui.QPushButton(Form)
        self.submit.setGeometry(QtCore.QRect(370, 320, 161, 41))
        self.submit.setObjectName("submit")
        
        self.submit.connect(self.submit, QtCore.SIGNAL("clicked()"), self.form_enviroment)
        
        self.abort = QtGui.QPushButton(Form)
        self.abort.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.abort.setGeometry(QtCore.QRect(190, 320, 181, 41))
        self.abort.setObjectName("abort")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def form_enviroment(self):

        dict_enviroment = {'name':'','path':'','initials':'','description':''}
        dict_enviroment['name'] = str(self.name_enviroment.text())
        dict_enviroment['path'] = str(self.path_enviroment.text())
        dict_enviroment['initials'] = str(self.initials_enviroment.text())
        dict_enviroment['description'] = str(self.description_enviroment.toPlainText())

        urlRequest.new_enviroment(dict_enviroment)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Criar Novo Coligado", None, QtGui.QApplication.UnicodeUTF8))
        self.Enviroment.setText(QtGui.QApplication.translate("Form", "Nome do Coligado", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "URL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Iniciais", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Descrição", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setText(QtGui.QApplication.translate("Form", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.abort.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        ui = QtGui.QWidget()
        f = Ui_Form()
        f.setupUi(ui)
        ui.show()
        sys.exit(app.exec_())
