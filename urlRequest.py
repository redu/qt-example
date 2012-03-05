#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
from urllib import urlencode
import simplejson
import requests

def list_json(resource):
        url = 'http://0.0.0.0:3000/api/'
        url = url + resource + '.json'
        f = urllib.urlopen(url)
        global result
        result = simplejson.loads(f.read())
        return result


def list_related():
    global listRelated
    listRelated = []
    for iterate in list_json('environments'):
        listRelated.append(iterate)
        
    return listRelated

def get_courses(env_name):
        for iterate in list_json('environments'):
                  if iterate['name'] == env_name:
                          global course_id
                          course_id = iterate['id']
        return list_json('environments/' + str(course_id) + '/courses')
        
def get_spaces(env_path):
        return list_json('courses/' + str(env_path) + '/spaces')

def get_user_gang(course_current):
    users = []
    list_users = simplejson.loads(urllib.urlopen('http://127.0.0.1:3000/api/courses/'+ str(course_current) +'/enrollments.json').read())
    for iterate in list_users:
        for it in iterate['links']:
            if it['rel'] == 'user':
                last_json = simplejson.loads(urllib.urlopen(str(it['href'])+'.json').read())
                users.append(last_json)
                
    return users

def new_enviroment(dict_enviroment):
        params = simplejson.dumps({'environment': dict_enviroment })
        url = "http://127.0.0.1:3000/api/environments"
        headers = {'content-type':'application/json'}
        result = requests.post(url, data=params, headers=headers)
        return result

def new_form(dict_form, current, name_form):
    if name_form == 'Curso':
        for iterate in list_related():
            if iterate['name'] == current:
                params = simplejson.dumps({'course': dict_form })
                url = "http://127.0.0.1:3000/api/environments/" + str(iterate['id']) + "/courses"
                headers = {'content-type':'application/json'}
                result = requests.post(url, data=params, headers=headers)
                return result

    elif name_form == 'Disciplina':
        for iterate in get_courses(current):
            if iterate['name'] == current:
                params = simplejson.dumps({'space': dict_form })
                url = "http://127.0.0.1:3000/api/courses/" + str(iterate['id']) + "/spaces"
                headers = {'content-type':'application/json'}
                result = requests.post(url, data=params, headers=headers)
                return result
                
def update_form(dict_any, current, name_form):

    if name_form == 'Coligado':
        for iterate in list_related():
            if iterate['name'] == current:
                params = simplejson.dumps({'environment': dict_any })
                url = "http://127.0.0.1:3000/api/environments/" + str(iterate['id'])
                                
    elif name_form == 'Curso':
        for iterate in get_courses(current):
            if iterate['name'] == current:
                params = simplejson.dumps({'course': dict_any })
                url = "http://127.0.0.1:3000/api/courses/" + str(iterate['id'])
                   
    elif name_form != 'Coligado' and name_form != 'Curso':
        for iterate in get_spaces(name_form):
            if iterate['name'] == current:
                params = simplejson.dumps({'space': dict_any })
                url = "http://127.0.0.1:3000/api/spaces/" + str(iterate['id'])
               
    headers = {'content-type':'application/json'}
    result = requests.put(url, data=params, headers=headers)
    return result
               
def kill_current(form_name,current):

    if form_name == 'Coligado':
        for iterate in list_related():
            if iterate['name'] == current:
                url = "http://127.0.0.1:3000/api/environments/" + str(iterate['id'])
                                
    elif form_name == 'Curso':
        for iterate in get_courses(current):
            if iterate['name'] == current:
                url = "http://127.0.0.1:3000/api/courses/" + str(iterate['id'])
         
    elif form_name == 'Turma':
        for iterate in current['links']:
            if iterate['rel'] == 'enrollments':
                ID = simplejson.loads(urllib.urlopen(str(iterate['href'])+'.json').read())
                for it in ID:
                    url = "http://127.0.0.1:3000/api/enrollments/" + str(it['id'])
                    
    else:
        for iterate in get_spaces(form_name):
            if iterate['name'] == current:
                url = "http://127.0.0.1:3000/api/spaces/" + str(iterate['id'])
    
    result = requests.delete(url)
    return result
