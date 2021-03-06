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

# 拡張子の種類でファイルに仕分けを行う
def classify(sorce_path):
    # configファイルを開く
    json_load = None
    with open("config.json","r") as json_file:
        json_load = json.load(json_file)

    # 入力ディレクトリのファイルをループで処理する
    for file in os.listdir(sorce_path):
        base, ext = os.path.splitext(file)
        # 拡張子の種類ごとに仕分けを行う
        for key in json_load:
            # 移動先のディレクトリ名
            directory_name = sorce_path + "/" + key + "/"
            os.makedirs(directory_name, exist_ok=True)
            # 類似した拡張子を調べる
            for value in json_load[key]:
                # valueと同じ拡張子のファイルがあれば移動する
                if ext == "."+value:
                    shutil.move(sorce_path+"/"+file, directory_name)

def main():
    args = sys.argv
    # 引数がない場合
    if len(args) < 2:
        print('error: Arguments are too short')
        return
    source_path = args[1]
    if(not check_directorypath(source_path)):
        return

    # 仕分けを行う
    classify(source_path)

if __name__ == '__main__':
    sys.exit(main())

