#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import shutil
import json

# 引数がディレククトリのパスなら返す
def get_directorypath(sorce_payh):
    # 引数のパスが存在しない場合
    if not os.path.exists(sorce_payh):
        print(sorce_payh + " is not found")
        return
    # 引数のパスがディレクトリではない場合
    if not os.path.isdir(sorce_payh):
        print( sorce_payh + " is not directory")
        return
    return sorce_payh

# if __name__ == '__main__':

 