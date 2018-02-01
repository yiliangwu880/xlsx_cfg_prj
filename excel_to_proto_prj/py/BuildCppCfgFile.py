#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
import base
import cfg

def BuildCfgCppStr(excel_name):
#创建cfg_h
##########################################################
    h_str ='''
#pragma once

#include <string>
#include <map>

struct C''' + excel_name + ''' 
{
'''
    fields_str = ''
    str_key_type = ''
    excel_info = cfg.g_all_sheets[excel_name]
    field = excel_info.field_dict[0]
    str_key_type = cfg.type_2_cpp_type[field.type_name]
    for idx in range(excel_info.ncols):
        field = excel_info.field_dict[idx]
        fields_str = "  " + cfg.type_2_cpp_type[field.type_name] + '  ' + field.identify + ';\n'
        h_str += fields_str

    t ='''
};

class ''' + excel_name + '''Mgr
{
public:
    static ''' + excel_name + '''Mgr &Instance();
	void ReadCfg();
	C''' + excel_name + ''' *Get(long key);

private:
    ''' + excel_name + '''Mgr(){};

private:
	std::map<''' + str_key_type + ''', C''' + excel_name + '''> m_key_2_data;
};    
    '''
    h_str+=t
##########################################################

#创建cfg_cpp
##########################################################

    fields_str = ''
    excel_info = cfg.g_all_sheets[excel_name]
    if excel_info.ncols < 1:
        print 'error excel info. ncols must >=1'
        return
    
    field = excel_info.field_dict[0]
    key_field_str = field.identify.lower()
    for idx in range(excel_info.ncols):
        field = excel_info.field_dict[idx]
        fields_str += r'        d.' + field.identify + r' = row.'+ field.identify.lower() + '();\n'
        

    cpp_str ='''
#include "''' + excel_name + '''.h"
#include "cfg_mgr.h"
#include "''' + cfg.cpp_proto_h_dir + excel_name + '''.pb.h"
#include <fstream>

using namespace std;

#define BYTES_FILE "''' + cfg.cpp_byte_file_dir + excel_name + '''.bytes"

''' + excel_name + '''Mgr & ''' + excel_name + '''Mgr::Instance()
{
	static ''' + excel_name + '''Mgr obj;
	return obj;
}

void ''' + excel_name + r'''Mgr::ReadCfg()
{
	''' + excel_name + r''' msg;
	if (!CfgUtility::ParseFromFileName(BYTES_FILE, msg))
	{
		printf("load '%s' fail\n", BYTES_FILE);
		return;
	}
	int n = msg.rows().size();
	for (int i = 0; i < n; i++)
	{
		const auto &row = msg.rows(i);
		C''' + excel_name + r'''  &d = m_key_2_data[row.''' + key_field_str + '''()];
''' + fields_str + '''
	}
}

C''' + excel_name + ''' *''' + excel_name + '''Mgr::Get(long key)
{
	auto it = m_key_2_data.find(key);
	if (it == m_key_2_data.end())
	{
		return nullptr;
	}
	return &(it->second);
}

    
    '''   
##########################################################
    return cpp_str, h_str

