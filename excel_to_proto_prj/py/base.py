#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
import xlrd
import shutil
import re
import codecs
import time
import datetime

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class struct:
    '''创建动态对象用'''
    pass

#重定向输出文件
def SetStdOutFile(*p):
    temp = sys.stdout
    sys.stdout = open('.server_all','w')
    print 1,2,3 # 测试，之后可以检查下.server_all 文件
    sys.stdout.close()
    sys.stdout = temp #resotre print
    print 1,2,3 # 测试
 
def StrToLong(s):
    try:
        return long(s)
    except:
        return 0

#返回目录所有文件路径 列表
def search(base):
    return SearchFile(base, '.xlsx')


def SearchFile(path, pattern):
    '''
    返回目录所有文件路径 列表,例如
        SearchFile（'./', '.xlsx')
    '''
    fileresult = []
    cur_list = os.listdir(path)
    for item in cur_list:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            fileresult += search(full_path)
        if os.path:
            if full_path.endswith(pattern):
                fileresult.append(full_path)
    return fileresult  
  
def get_key_arg(name):
    value = xls_lua_config.lua_config_table.get(name)
    #没找到，按照默认格式来，列表样式
    if not value:
        return [], None
    
    #找到了，
    return value["key"], value["func"]

def check_generate(gen_type, name):
    value = server_xlsm_convert_config.convert_config.get(name)
    #没找到，按照默认格式来，列表样式
    if not value:
        return False
    
    #找到了，
    if (gen_type == "bytes"):
        return value[0]
    elif (gen_type == "lua"):
        return value[1]
    else:
        return False

def strToDate(str):
    if(str==""):
        str="0";
    str=str.strip();
    strArr=str.split('/');
    temp=["0","0","0","0","0","0"];
    for i in range(0,len(temp)):
        if(i<len(strArr)):
            temp[i]=strArr[i];
    result='';
    if(temp[0]=="0"):
        return 0;
    else:
        for i in range(0,len(temp)):
            if(i<2):
                result=result+temp[i]+'-';
            elif(i==2):
                result=result+temp[i]+' ';
            elif(i<5):
                result=result+temp[i]+':';
            else:
                result=result+temp[i];
        #print result 
        timeStamp=time.mktime(time.strptime(result,'%Y-%m-%d %H:%M:%S'));
        return int(timeStamp);

if __name__ == '__main__':
    print 'test base'
