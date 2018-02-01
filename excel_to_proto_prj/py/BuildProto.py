#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
根据excel 文件 ，生成 proto文件

proto格式参考：

option optimize_for = CODE_SIZE;

message Cfg_activity {
    message Row {
        optional int32 id = 1;
        optional string name = 2;
        ...
    }
    repeated Row rows = 1;
}
'''


import os,sys
import xlrd
import base
import cfg

class g_cfg:
    '''全局配置'''
    excel_dir=1
    proto_dir=1

def GetFieldList(sheet):
    '''
    返回域列表，例如 [
                    {"id":"idname", "type":"int", "describe":"说明",},
                    ...
                 ]
    '''
    ret=[]
    for c in range(sheet.ncols):
        field = {}
        field["id"] = sheet.cell(0,c).value
        t = sheet.cell(1,c).value
        if not cfg.cfg_old_type.has_key(t):
            print 'error type name in cell' + t
            return
        replace = cfg.cfg_old_type[t]
        field["type"] = replace
        field["describe"] = sheet.cell(2,c).value

        ret.append(field)
    return ret

def BuildExcelInfo(field_ls, excel_info, ncols):
    '''生成 g_all_sheets 配置 '''
    field_dict = {}
    excel_info.field_dict = field_dict
    excel_info.date_start_row = 3
    excel_info.ncols = ncols

    idx = 0
    for field in field_ls:
        cfg_filed = base.struct()
        field_dict[idx] = cfg_filed
        cfg_filed.type_name = field["type"]
        if not cfg.type_2_py_type.has_key(cfg_filed.type_name):
            print 'no py type for ' + cfg_filed.type_name
            continue
        cfg_filed.py_type_name = cfg.type_2_py_type[cfg_filed.type_name]
        cfg_filed.py_convert_fun = cfg.type_2_py_convert_fun[cfg_filed.type_name]
        cfg_filed.identify = field["id"]
        idx = idx + 1


def BuildProtoStr(field_ls, excelname):
    '''
    生成 proto文件的字符串
    para field_ls 域列表，例如 [
                    {"id":"idname", "type":"int", "describe":"说明",},
                    ...
                 ]
    
    '''
    s = 'option optimize_for = CODE_SIZE;\n\nmessage ' + excelname + ' {\n'\
    '    message Row {\n'

    idx = 1
    for field in field_ls:
        t = '       optional '+field["type"]+" "+field["id"] + " = "+ str(idx) + ";\n"
        s += t
        idx = idx + 1

    s += r'''
    }

    repeated Row rows = 1;
}'''
    return s

def BuildExcelFile(excel_file):
    excelname = os.path.basename(excel_file).replace(".xlsx", "")
    dirname = os.path.dirname(excel_file)
    a = xlrd.open_workbook(excel_file)
    proto_filename = excelname+'.proto'

    excel_info = base.struct()
    cfg.g_all_sheets[excelname]= excel_info
    excel_info.sheets = a.sheets()
    
    for sheet in a.sheets():
        field_ls=GetFieldList(sheet)
        if not field_ls:
            print 'build ' + excelname + "fail"
            break
        BuildExcelInfo(field_ls, excel_info, sheet.ncols) 
        s=BuildProtoStr(field_ls, excelname)
        file = open(g_cfg.proto_dir + "/" + proto_filename, 'w')
        file.write(s)
        file.close()
        break  # 只去第一个表

def Build(excel_path, proto_path):
    g_cfg.excel_dir = excel_path
    g_cfg.proto_dir = proto_path
    for excel_file in base.search(excel_path):
        print '> %s' % os.path.basename(excel_file)
        BuildExcelFile(excel_file)
        

