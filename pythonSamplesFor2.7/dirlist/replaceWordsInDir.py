# -*- coding: utf-8 -*- 
import os

replaceList = [("room", "space"),
               ("Room", "Space"),
               ("ROOM", "SPACE")]

def loadDirs(rootDir): 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        print 'loading directory: ',path
        if path.find('.svn') != -1:
        	continue
        if os.path.isfile(path):
         	# print 'this is file'
         	doreplace(path)
        if os.path.isdir(path): 
            loadDirs(path) 
def doreplace(fileExpression):
    # fileExpression = raw_input ("Please input file to be replaced :")
    print 'start doreplace----------------','filename',fileExpression
    fd = open(fileExpression,'r')
    content = fd.read()
    # print content
    for oldValue, newValue in replaceList:
    	content = content.replace(oldValue, newValue)
    # print content
    fd.close
    fd = open(fileExpression,'w')
    fd.write(content)
    fd.close
fileExpression = raw_input ("Please input dir to be processed :")
loadDirs(fileExpression)