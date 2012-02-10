#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import simplejson

def list_json(resource):
    url = 'http://0.0.0.0:3000/api/'
    url = url + resource + '.json'
    f = urllib.urlopen(url)
    global result
    result = simplejson.loads(f.read())
    return result

listRelated = []
for iterate in list_json('environments'):
        listRelated.append(iterate['name'])

def get_courses(env_name):
        for iterate in list_json('environments'):
                  if iterate['name'] == env_name:
                          course_id = iterate['id']
        return list_json('environments/' + str(course_id) + '/courses')
        
def get_spaces(env_name):
        for iterate in result:
                  if iterate['name'] == env_name:
                          Id = iterate['id']
        return list_json('courses/' + str(Id) + '/spaces')
