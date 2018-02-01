#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
import base
import cfg
import BuildCppCfgFile
import BuildCppCfgMgrFile







def BuildCfgCpp():
    all_excel_name = []
    for excel_name in base.SearchFile(cfg.out_proto_dir, ".proto"):
        excel_name = os.path.basename(excel_name)
        excel_name =excel_name.replace(".proto", "")
        cpp_str, h_str =  BuildCppCfgFile.BuildCfgCppStr(excel_name)
        file = open(cfg.out_cpp_dir + "/" + excel_name + '.cpp', 'w')
        file.write(cpp_str)
        file.close()
        file = open(cfg.out_cpp_dir + "/" + excel_name + '.h', 'w')
        file.write(h_str)
        file.close()
        all_excel_name.append(excel_name)

    cpp_str, h_str =  BuildCppCfgMgrFile.BuildCfgMgrCpp(all_excel_name)
    file = open(cfg.out_cpp_dir + '/cfg_mgr.cpp', 'w')
    file.write(cpp_str)
    file.close()
    file = open(cfg.out_cpp_dir + '/cfg_mgr.h', 'w')
    file.write(h_str)
    file.close()
    
def Build():
    BuildCfgCpp()
    print 'build cpp'