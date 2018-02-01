#!/usr/bin/python

import os
import filecmp
import sys
import shutil

#list files

def filter(filePath):
    if filePath.endswith(r'.cc') or filePath.endswith(r'.h'):

        return True

    return False

def copyFiles(srcFile,  dstFile):

    if os.path.exists(srcFile):

        cmd_str = "cp -p %s %s"%(srcFile, dstFile)

        print cmd_str
        os.system(cmd_str)

def listFiles(dirPath):

    fileList=[]

    for _,_,files in os.walk(dirPath):

        for fileObj in files:

            if filter(fileObj):
                #fileList.append(os.path.join(curPath,fileObj))
                fileList.append(fileObj)

    return fileList

def convert(dirPath, tmpPath):

    oldPath = os.getcwd()

    os.chdir(dirPath)

    curPath = os.getcwd()

    #get file list
    oldList = listFiles(tmpPath)

    newList = []

    for fileObj in oldList:
        newList.append(tmpPath + fileObj)

    length = len(oldList)

    for i in xrange(length):

        if not os.path.exists(newList[i]):
            print "convert %s fail, check the file" %newList[i]

            continue

        if not os.path.exists(oldList[i]):
            copyFiles(newList[i],  oldList[i])

        if not filecmp.cmp(newList[i], oldList[i]):
            copyFiles(newList[i],  oldList[i])


    os.chdir(oldPath)

def generate_protoc(src):

    protoc_str = r'./protoc ./%s/*.proto --cpp_out=./  -I=./'%(src)
    print protoc_str

    tmp_dir = r'../../tmp/'

    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)

    os.system(protoc_str)

    dir_str = r"./%s" %(src)
    tmp_str = r"../../../tmp/protocol/%s/" %(src)

    convert(dir_str, tmp_str)

def main():

    tmp_dir = "../../tmp/protocol"
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    # generate_protoc("chat")
    # generate_protoc("comm")
    # generate_protoc("conn")
    # generate_protoc("dir")
    # generate_protoc("dbproxy")
    # generate_protoc("account")
    # generate_protoc("offlinesvrd")
    # generate_protoc("ranksvrd")
    generate_protoc("cfg_proto")

if __name__=='__main__':

    main()
