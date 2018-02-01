#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
import base
import cfg

def BuildCfgMgrCpp(all_excel_name):
##################### mgr h #####################################

    str_include = ''
    str_get_cfg_declare = ''
    str_read_cfg = ''
    str_get_cfg_def = ''
    for excel_name in all_excel_name:
        excel_info = cfg.g_all_sheets[excel_name]
        if excel_info.ncols < 1:
            print 'error excel info. ncols must >=1'
            continue
        key_field = excel_info.field_dict[0]
        str_key_type = cfg.type_2_cpp_type[key_field.type_name]

        str_include += r'#include  "' + excel_name + '.h"\n'
        str_read_cfg += '   ' + excel_name + 'Mgr::Instance().ReadCfg();\n'
        str_get_cfg_declare += '    C' + excel_name +  r'* ' + excel_name + '(' + str_key_type  + ' key );\n'
        str_get_cfg_def += '''
C''' + excel_name + '''* CfgMgr::''' + excel_name + '''(''' + str_key_type  + ''' key)
{
    C''' + excel_name + ''' *p = ''' + excel_name + '''Mgr::Instance().Get(key);
    if (nullptr)
    {
        if (nullptr != CfgMgr::find_fail_cb)
        {
	        (*CfgMgr::find_fail_cb)("''' + excel_name + '''", key);
        }
    }
    return p;
}
'''

    h_str=r'''
#pragma once
''' + str_include + '''
#include <string>
#include "google/protobuf/message.h"

typedef void (*FindCfgFailCB)(const std::string &cfg_name, long key);

class CfgMgr
{
public:
    static CfgMgr &Instance()
    {
        static CfgMgr obj;
        return obj;
    }
    void Init();
''' + str_get_cfg_declare + '''
    FindCfgFailCB find_fail_cb;
private:
    CfgMgr(){find_fail_cb=nullptr;}
};

struct CfgUtility
{
	static bool ParseFromFileName(const std::string& filename, google::protobuf::Message& pbm);

};
    '''

##################### mgr cpp #####################################
    cpp_str = r'''
#include "cfg_mgr.h"
#include <string>
#include <fstream>

using namespace std;

bool CfgUtility::ParseFromFileName(const std::string& filename, google::protobuf::Message& pbm)
{
	std::ifstream ifs(filename.c_str());
	if (!ifs.is_open())
	{
		printf("open file fail. %s", filename.c_str());
		return false;
	}
	if (!pbm.ParseFromIstream(&ifs))
	{
		ifs.close();
		return false;
	}
	ifs.close();
	return true;
}

void CfgMgr::Init()
{
''' + str_read_cfg + '''
}
''' + str_get_cfg_def

    return cpp_str, h_str





