#!/usr/bin/python
# -*- coding: utf-8 -*-


import os,sys
import base

'''
写配置
'''


excel_dir = r"../excel"
out_proto_dir = r"../out/proto/"
out_cpp_dir=r"../out/cpp"
out_lua_dir=r"../out/lua"
temp_py_proto_dir=r"../temp/proto_py"

#生成cpp文件相关配置
cpp_proto_h_dir =r'cfg_proto/'   #cpp项目，proto h文件的路径 ，
cpp_byte_file_dir =r'../ccp_read_cfg_prj/cfg_proto/'


#exce类型字符 转换 成proto类型
cfg_old_type ={
    'INTEGER':'uint32',  
    'varchar(32)':'string',
    'varchar(7)':'string',
    'varchar(8)':'string',
    'uint32':'uint32',
    'string':'string',
    'int32':'int32',
    'uint64':'uint64',
    'int64':'int64'
}

#proto类型 2 py类型字符串
type_2_py_type ={
    'uint32':'long',
    'string':'str',
    'int32':'long',
    'uint64':'long',
    'int64':'long'
}

#proto类型 2 py类型转换函数
type_2_py_convert_fun ={
    'uint32':'base.StrToLong',
    'string':'str',
    'int32':'base.StrToLong',
    'uint64':'base.StrToLong',
    'int64':'base.StrToLong'
}

#proto类型 2 cpp类型字符串
type_2_cpp_type ={
    'uint32':'unsigned long',
    'string':'std::string',
    'int32':'long',
    'uint64':'unsigned long long',
    'int64':'long long'
}

'''g_all_sheets 所有excel信息, 结构:
    struct = 
    {
    "excel文件名无后缀": excel_info,
    ..
    }

    excel_info= struct
    {
        sheets = sheets对象
        field_dict=  idx 2 field
        date_start_row = 2 #数据开始行索引
        ncols = 第一个表的列数
    }

    field = struct
    {
        identify = 标示符，域名
        type_name = proto数据类型
        py_type_name = 对应py的数据类型
        py_convert_fun = 转换字符串数据的函数
    }
'''
g_all_sheets = {}