#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
import BuildProto
import BuildBytes
import BuildCpp
import BuildLua
import base
import shutil
import cfg


def SetEnv():
    os.system('set_env.bat')

if __name__ == '__main__':
    #SetEnv()
    #清理旧文件
    for f in base.SearchFile(cfg.out_proto_dir, ''):
        os.remove(f)
    for f in base.SearchFile(cfg.temp_py_proto_dir, ''):
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)


    BuildProto.Build(cfg.excel_dir, cfg.out_proto_dir)

    BuildBytes.Build(cfg.excel_dir, cfg.out_proto_dir, cfg.out_proto_dir)

    BuildCpp.Build()
    BuildLua.Build()
    print 'done'