#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import shutil
import json

# 引数がディレククトリのパスなら返す
def check_directorypath(sorce_path):
    result = True
    # 引数のパスが存在しない場合
    if not os.path.exists(sorce_path):
        print("error: " + sorce_path + " is not found")
        result = False
    # 引数のパスがディレクトリではない場合
    if not os.path.isdir(sorce_path):
        print("error: " + sorce_path + " is not directory")
        result = False
    return result

# if __name__ == '__main__':

