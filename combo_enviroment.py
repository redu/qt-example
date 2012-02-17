#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ComboBox
"""

import sys
from PyQt4 import QtGui, QtCore
import urlRequest


class ComboBox(QtGui.QWidget):
    def __init__(self):
        super(ComboBox, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.lbl = QtGui.QLabel("", self)
        combo = QtGui.QComboBox(self)
        for iterate in urlRequest.listRelated:
                combo.addItem(iterate['name'])

        combo.move(50, 50)
        self.lbl.move(50, 100)
        combo.activated[str].connect(self.onActivated)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('QtGui.QComboBox')
        self.setWindowTitle('Cursos')
        self.show()
        
    def onActivated(self, text):
        global value
        value = text
        self.lbl.setText(text)
        self.lbl.adjustSize()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ComboBox()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
