#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from main_window import Ui_MainWindow
import urlRequest       



# OBS: todos os ENVIRONMENTS estao escritos sem o n

class APIWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.setupUi(self)
        
        self.connect(self.enviroment, QtCore.SIGNAL('clicked()'),self.related)
        self.connect(self.course, QtCore.SIGNAL('clicked()'),self.course_related)
        self.connect(self.discipline, QtCore.SIGNAL('clicked()'),self.discipline_related)
        
#         Ainda nao foi criado o metodo de matricula
#        self.connect(self.turma, QtCore.SIGNAL('clicked()'),self.gang)

        self.connect(self.submit_ok, QtCore.SIGNAL('clicked()'),self.new)
        self.connect(self.edit, QtCore.SIGNAL('clicked()'),self.update)

#   Funcao lista Coligado     
    def related(self):
        global event
        event = False
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
        content = urlRequest.list_related()
        for iterate in content:
            self.comboBox.addItem(iterate['name'])
                               
        self.comboBox.activated[str].connect(self.onActivated_coligado)
        for iterate in content:
            self.listWidget.addItem(iterate['name'])
    
    def onActivated_coligado(self, text):
        self.listWidget.clear()
        self.listWidget.addItem(text)
        global current
        current = text
        
#   Funcao lista cursos depende do Coligado selecionado
    
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
        
        if current:
            content = urlRequest.get_courses(current)
            if content == []:
                self.listWidget.addItem('Nao ha curso cadastrado')
            else:
                for iterate in content:
                        self.comboBox.addItem(iterate['name'])
                        self.listWidget.addItem(iterate['name'])
                self.comboBox.activated[str].connect(self.onActivated_courses)            
#        else:
#            self.listWidget.addItem('Click em Coligados e escolha um Coligado no ComboBox')

    def onActivated_courses(self, text):
        self.listWidget.clear()
        self.listWidget.addItem(text)
        content = urlRequest.get_courses(current)

        for iterate in content:
            if text == iterate['name']:
                global course_current
                course_current = iterate['path']
               
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
        if self.checkBox_path.checkState() == 2:
            self.checkBox_path.animateClick()
        if self.checkBox_initials.checkState() == 2:
            self.checkBox_initials.animateClick()
        if self.checkBox_workload.checkState() == 2:
            self.checkBox_workload.animateClick()
        if self.checkBox_description.checkState() == 0:
            self.checkBox_description.animateClick()
            
        self.workload.setText('')

        if current:
            discipline = urlRequest.get_spaces(course_current)
            if discipline != []:
                for iterate in discipline:
                   self.comboBox.addItem(iterate['name'])
                   self.listWidget.addItem(iterate['name'])
            else:
                self.listWidget.addItem('Nao ha disciplinas cadastradas')
        self.comboBox.activated[str].connect(self.onActivated_discipline)            
        
    def onActivated_discipline(self, text):
        self.listWidget.clear()
        self.listWidget.addItem(text)
        
# ============================================================
#       metodo update
#
    def update(self):
        global event
        event = True
        form_name = str(self.lineEdit_2.text())
        if form_name == 'Coligado':
            content = urlRequest.list_related()
            for iterate in content:
                if iterate['name'] == current:
                    self.name.setText(iterate['name'])
                    self.path.setText(iterate['path'])
                    self.initials.setText(iterate['initials'])
                    if iterate['description'] and iterate['description'] != []:
                        self.description.setText(iterate['description'])
                    
        elif form_name == 'Curso':
            content = urlRequest.get_courses(current)
            for iterate in content:
                if iterate['name'] == current:
                    self.name.setText(iterate['name'])
                    self.path.setText(iterate['path'])
                    if iterate['workload'] and iterate['workload'] != []:
                        self.workload.setText(str(iterate['workload']))
                    if iterate['description'] and iterate['description'] != []:
                        self.description.setText(iterate['description'])

        elif form_name == 'Disciplina':
            content = urlRequest.get_spaces(course_current)
            for iterate in content:
                if iterate['name'] == current:
                    self.name.setText(iterate['name'])
                    if iterate['description'] and iterate['description'] != []:
                        self.description.setText(iterate['description'])


    def new(self):
    
#       Butao Ok para o metodo update
#  =============================================================================
    
        if event:
            form_name = str(self.lineEdit_2.text())
            def clear_form():
                self.name.setText('')
                self.workload.setText('')
                self.textEdit.setText('')
                self.path.setText('')
                self.initials.setText('')
            
            if form_name == 'Coligado':
                dict_environment = {'name':'','path':'','initials':'','description':''}            
                dict_environment['name'] = str(self.name.text())            
                dict_environment['path'] = str(self.path.text())
                dict_environment['initials'] = str(self.initials.text())
                if str(self.textEdit.toPlainText()) != 'Optional':
                    dict_environment['description'] = str(self.textEdit.toPlainText())
           
                urlRequest.update_form(dict_environment, current, form_name)
                self.listWidget.addItem('O coligado foi atualizado com sucesso')

                clear_form()
                self.listWidget.clear()
                self.listWidget.addItem('Coligado atualizado')
            
            elif form_name == 'Curso':
                dict_course = {'name':'','path':'','workload':'','description':''}            
                dict_course['name'] = str(self.name.text())            
                dict_course['path'] = str(self.path.text())
                if str(self.workload.text()) != 'Optional':
                    dict_course['workload'] = str(self.workload.text())
                if str(self.textEdit.toPlainText()) != 'Optional':
                    dict_course['description'] = str(self.textEdit.toPlainText())
                
                urlRequest.update_form(dict_course,current, form_name)
                self.listWidget.addItem('O curso foi atualizado')

                clear_form()
                self.listWidget.clear()
       
            elif form_name == 'Disciplina':
                dict_discipline = {'name':'','description':''}
                dict_discipline['name'] = str(self.name.text())            
                dict_discipline['description'] = str(self.textEdit.toPlainText())
                
                result = urlRequest.update_form(dict_discipline,current, course_current)
                self.listWidget.addItem('A disciplina foi atualizada')

                clear_form()
                self.listWidget.clear()
#
# =========================================================================
#       Butao Ok para o metodo new

        else:
            form_name = str(self.lineEdit_2.text())
            def clear_form():
                self.name.setText('')
                self.workload.setText('')
                self.textEdit.setText('')
                self.path.setText('')
                self.initials.setText('')
            
            if form_name == 'Coligado':
#            Cadastra coligado
                dict_enviroment = {'name':'','path':'','initials':'','description':''}            
                dict_enviroment['name'] = str(self.name.text())            
                dict_enviroment['path'] = str(self.path.text())
                dict_enviroment['initials'] = str(self.initials.text())
                dict_enviroment['description'] = str(self.textEdit.toPlainText())
           
                result = urlRequest.new_enviroment(dict_enviroment)
                self.listWidget.addItem('Novo coligado adicionado')

                clear_form()
                self.listWidget.clear()
                
            
            elif form_name == 'Curso':
#            Cadastra curso            
                dict_course = {'name':'','path':'','workload':'','description':''}            
                dict_course['name'] = str(self.name.text())            
                dict_course['path'] = str(self.path.text())
                dict_course['workload'] = str(self.workload.text())
                if str(self.textEdit.toPlainText()) != 'Optional':
                    dict_course['description'] = str(self.textEdit.toPlainText())
                
                result = urlRequest.new_form(dict_course,current,form_name)
                self.listWidget.addItem('Novo curso cadastrado')
                    
                clear_form()
                self.listWidget.clear()
       
            elif form_name == 'Disciplina': 
#            Cadastra disciplina
                dict_discipline = {'name':'','description':''}
                dict_discipline['name'] = str(self.name.text())            
                dict_discipline['description'] = str(self.textEdit.toPlainText())
                
                result = urlRequest.new_form(dict_discipline,current,form_name)
                self.listWidget.addItem('Nova disciplina cadastrada')
                    
                clear_form()
                self.listWidget.clear()


      
      
app = QtGui.QApplication(sys.argv)
form = APIWindow()
form.show()
app.exec_()
