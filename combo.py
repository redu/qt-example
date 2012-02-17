#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ComboBox
"""

import sys
from PyQt4 import QtGui, QtCore
import ui_form
import edit_enviroment

def edit_form_enviroment(self):
    if self == 'Coligado':
        pass
#        form = edit_enviroment.main()

class ComboBox(QtGui.QWidget):
    
    def __init__(self):
        super(ComboBox, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.lbl = QtGui.QLabel("", self)
        combo = QtGui.QComboBox(self)

        combo.addItem("Coligado")
        combo.addItem("Curso")
        combo.addItem("Disciplina")
        combo.addItem("Turma")

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)        
         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QtGui.QComboBox')
        self.show()
        
    def onActivated(self, text):
        global value
        value = text
        edit_form_enviroment(value)
        self.lbl.setText(text)
        self.lbl.adjustSize()  
          
                  
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ComboBox()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
