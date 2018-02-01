#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
import base
import platform
import cfg

class g_cfg:
    '''全局配置'''
    excel_dir=1
    proto_dir=1
    bytes_dir=1

'''所有导入proto py 模块信息,结构:
[m_info,...]
每个m_info结构: {
                'name':module_name ,
                'module':proto_py_m,
        }
'''
all_proto_py_module = []


def Build(excel_path, proto_path, bytes_path):
    g_cfg.excel_dir = excel_path
    g_cfg.proto_dir = proto_path
    g_cfg.bytes_dir = bytes_path
    BuildProtoPy()
    ImportAllProtoPy()
    BuildAllBytesFile()

def BuildProtoPy():
    proto_dir = g_cfg.proto_dir
    proto_py_dir = cfg.temp_py_proto_dir
    proto_list = os.listdir(proto_dir)
    for item in proto_list:
        #proto执行不行，就去安装吧。
        if 'Linux' in platform.system():
            to_python_cmd = 'protoc --python_out=' + proto_py_dir + ' --proto_path=' + proto_dir + ' ' + proto_dir + item
        else:
            to_python_cmd = 'protoc.exe --python_out=' + proto_py_dir + ' --proto_path=' + proto_dir + ' ' + proto_dir + item
        os.system(to_python_cmd)

def ImportAllProtoPy():
    proto_list = os.listdir(cfg.temp_py_proto_dir)
    sys.path.append(cfg.temp_py_proto_dir) 
    print "import dir=",cfg.temp_py_proto_dir 
    for item in base.SearchFile(cfg.temp_py_proto_dir, ".py"):
        item = os.path.basename(item)
        print "import proto_py =", item
        module_name =item.replace(".py", "")
        proto_py_m = __import__(module_name) 
        m_info = {
                'name':module_name ,
                'module':proto_py_m,
        }
        all_proto_py_module.append(m_info)

def BuildBytesFile(module_name, module):
    excelname =module_name.replace("_pb2", "")
    exe_str = 'proto_obj=module.'+excelname+"()"
    exec exe_str  #module.proto类名()
    excel_info = cfg.g_all_sheets[excelname]
    sheet = excel_info.sheets[0] #去第一个sheet
    
    #生成 proto_obj
    for row in range(sheet.nrows):
        if row < excel_info.date_start_row: #描述不要
            continue
        row_obj = proto_obj.rows.add()
        for col in range(sheet.ncols):
            field = excel_info.field_dict[col]
            value = sheet.cell(row,col).value
            exec 'value = ' + field.py_convert_fun + '(value)'
            if field.py_type_name == 'str':
                value = unicode(value, "utf-8");
            exe_str = "row_obj." + field.identify + "= value"
            exec exe_str
    
    #序列化内容到byte文件
    f = file(g_cfg.proto_dir + excelname + '.bytes', 'wb')
    f.write(proto_obj.SerializeToString())
    f.close()

def BuildAllBytesFile():
    for m_info in all_proto_py_module:
        BuildBytesFile(m_info['name'], m_info['module'])
    print 'BuildAllBytesFile'