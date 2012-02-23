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
        self.connect(self.discipline, QtCore.SIGNAL('clicked()'),self.discipline_related)
#        self.name.setText('Filipe')
#        self.checkBox_form.animateClick()
#        self.connect(self.turma, QtCore.SIGNAL('clicked()'),self.gang)
        self.connect(self.submit, QtCore.SIGNAL('clicked()'),self.new)
        self.connect(self.edit, QtCore.SIGNAL('clicked()'),self.update)
        

    
    def related(self):
        self.listWidget.clear()
        self.comboBox.clear()
        if self.checkBox_form.checkState() == 2:
            pass
        else:
            self.checkBox_form.animateClick()        
            
        self.lineEdit_2.setText('Coligado')
        
        if self.checkBox_name.checkState() == 0:
            self.checkBox_name.animateClick()
        if self.checkBox_path.checkState() == 0:
            self.checkBox_path.animateClick()
        if self.checkBox_initials.checkState() == 0:
            self.checkBox_initials.animateClick()
        if self.checkBox_workload.checkState() == 2:
            self.checkBox_workload.animateClick()
        if self.checkBox_description.checkState() == 0:
            self.checkBox_description.animateClick()
        
        self.workload.setText('')
        self.textEdit.setText('Optional')
        content = urlRequest.listRelated
        for iterate in content:
            self.listWidget.addItem(iterate['name'])
            
    def course_related(self):
        self.listWidget.clear()
        self.comboBox.clear()
        if self.checkBox_form.checkState() == 2:
            pass
        else:
            self.checkBox_form.animateClick()
            
        self.lineEdit_2.setText('Curso')
        if self.checkBox_name.checkState() == 0:
            self.checkBox_name.animateClick()
        if self.checkBox_path.checkState() == 0:
            self.checkBox_path.animateClick()
        if self.checkBox_initials.checkState() == 2:
            self.checkBox_initials.animateClick()
        if self.checkBox_workload.checkState() == 0:
            self.checkBox_workload.animateClick()
        if self.checkBox_description.checkState() == 0:
            self.checkBox_description.animateClick()

        self.textEdit.setText('Optional')
        self.workload.setText('Optional')
        content = urlRequest.listRelated
        if content == []:
            self.listWidget.addItem('Não há cursos para esse coligado')
        else:
            for iterate in content:
                self.comboBox.addItem(iterate['name'])
                               
        self.comboBox.activated[str].connect(self.onActivated_courses)

    def discipline_related(self):
        self.listWidget.clear()
        self.comboBox.clear()
        if self.checkBox_form.checkState() == 2:
            pass
        else:
            self.checkBox_form.animateClick()
            
        self.lineEdit_2.setText('Disciplina')
        if self.checkBox_name.checkState() == 0:
            self.checkBox_name.animateClick()
        if self.checkBox_path.checkState() == 0:
            self.checkBox_path.animateClick()
        if self.checkBox_initials.checkState() == 2:
            self.checkBox_initials.animateClick()
        if self.checkBox_workload.checkState() == 2:
            self.checkBox_workload.animateClick()
        if self.checkBox_description.checkState() == 2:
            self.checkBox_description.animateClick()
            
        self.workload.setText('')
        for iterate in courses:
            self.comboBox.addItem(iterate['name'])

        self.comboBox.activated[str].connect(self.onActivated_discipline)
        
    def onActivated_discipline(self, text):
        self.listWidget.clear()
        discipline = urlRequest.get_spaces(text, courses)
        for iterate in discipline:
            self.listWidget.addItem(iterate['name'])
        
    def onActivated_courses(self, text):
        self.listWidget.clear()
        global courses
        courses = urlRequest.get_courses(text)
        if courses == []:
            self.listWidget.addItem('Não há cursos cadastradas para esse Coligado')
        for iterate in courses:
            self.listWidget.addItem(iterate['name'])
            
    def new(self):
        form_name = str(self.lineEdit_2.text())
        def clear_form():
            self.name.setText('')
            self.workload.setText('')
            self.textEdit.setText('')
            self.path.setText('')
            self.initials.setText('')
            
        if form_name == 'Coligado':
            dict_enviroment = {'name':'','path':'','initials':'','description':''}            
            dict_enviroment['name'] = str(self.name.text())            
            dict_enviroment['path'] = str(self.path.text())
            dict_enviroment['initials'] = str(self.initials.text())
            dict_enviroment['description'] = str(self.textEdit.toPlainText())
           
            urlRequest.new_enviroment(dict_enviroment)
            clear_form()
            self.listWidget.clear()
            self.listWidget.addItem('Novo coligado adicionado')
            
        elif form_name == 'Curso': # Falta selecionar o Coligado relacionado 
            dict_course = {'name':'','path':'','workload':'','description':''}            
            dict_course['name'] = str(self.name.text())            
            dict_course['path'] = str(self.path.text())
            dict_course['workload'] = str(self.workload.text())
            dict_course['description'] = str(self.textEdit.toPlainText())
            
            # Criar medoto e urlRequest para add novo curso
            clear_form()
            self.listWidget.clear()
            self.listWidget.addItem('Novo curso cadastrado')
       
        elif form_name == 'Disciplina':
            # Falta selecionar o Coligado relacionado 
            dict_discipline = {'name':'','path':''}
            dict_discipline['name'] = str(self.name.text())            
            dict_discipline['path'] = str(self.path.text())

            
            # Criar medoto e urlRequest para add nova disciplina
            clear_form()
            self.listWidget.clear()
            self.listWidget.addItem('Nova disciplina cadastrada')

    def update(self):
        pass
        


      
      
app = QtGui.QApplication(sys.argv)
form = APIWindow()
form.show()
app.exec_()
