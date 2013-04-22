# -*- coding: utf-8 -*- 
import os

replaceList = [("com.raiyun.common.finance.entity.curve", "com.raiyun.common.business.entity.curve")
               , ("com.raiyun.common.finance.entity","com.raiyun.common.business.entity")]
header = """
/*
 * Copyright (C) Shanghai Raiyun Financial Technologies Inc.  All Rights Reserved.
 */
"""
destFile = "d:\\codes.txt"

def loadDirs(rootDir): 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        print 'loading directory: ',path
        if path.find('.svn') != -1:
        	continue
        if os.path.isfile(path):
         	doreplace(path)
            # appendFileContent(path)
        if os.path.isdir(path): 
            loadDirs(path)
def readFileContent(fileExpression):
    print 'start readfile----------------','filename',fileExpression
    fd = open(fileExpression,'r')
    content = fd.read()
    fd.close
    return content
def doreplace(fileExpression):
    # fileExpression = raw_input ("Please input file to be replaced :")
    print 'start doreplace----------------','filename',fileExpression
    content = readFileContent(fileExpression)
    # print content
    for oldValue, newValue in replaceList:
    	content = content.replace(oldValue, newValue)
    # print content
    fd = open(fileExpression,'w')
    fd.write(content)
    fd.close
def appendFileContent(fileExpression):
    print 'appendFileContent---------',fileExpression
    content = readFileContent(destFile)
    content += header
    content += readFileContent(fileExpression)
    f = open(destFile,'w')
    f.write(content)
    f.close
def replaceKeyWordsInDir():
    fileExpression = raw_input ("Please input dir to be processed :")
    loadDirs(fileExpression)
replaceKeyWordsInDir()
    