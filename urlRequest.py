#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import simplejson

def list_json(resource):
    url = 'http://0.0.0.0:3000/api/'
    url = url + resource + '.json'
    f = urllib.urlopen(url)
    result = simplejson.loads(f.read())
    return result

listRelated = []

for x in list_json('environments'):
        listRelated.append(x['name'])

def get_courses(env_name):
        for x in list_json('environments'):
                  if x['name'] == env_name:
                          course_id = x['id']
        return list_json('environments/' + str(course_id) + '/courses')
        
