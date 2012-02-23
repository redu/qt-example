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

listRelated = []
for iterate in list_json('environments'):
        listRelated.append(iterate)

def get_courses(env_name):
        for iterate in list_json('environments'):
                  if iterate['name'] == env_name:
                          course_id = iterate['id']
        return list_json('environments/' + str(course_id) + '/courses')
        
def get_spaces(env_name, course):
        for iterate in course:
                  if iterate['name'] == env_name:
                          Id = iterate['id']
                          return list_json('courses/' + str(Id) + '/spaces')
        
def new_enviroment(dict_enviroment):
        params = simplejson.dumps({'environment': dict_enviroment })
        url = "http://127.0.0.1:3000/api/environments"
        headers = {'content-type':'application/json'}
        result = requests.post(url, data=params, headers=headers)

def update_enviroment(name_enviroment):
        for iterate in listRelated:
                if iterate['name'] == name_enviroment:
                        return iterate
