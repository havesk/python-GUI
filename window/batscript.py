# -*- coding=utf-8 -*-
import codecs
from subprocess import Popen
import sys
import os


class batscript:
    def __init__(self,batname):

        print("------batscript init-----")
        print(sys.getdefaultencoding())
        self.exebatname=batname
        self.fold_address="";
        #读取配置文件，获取根目录
        with codecs.open("../resource/config.property", 'r', 'utf-8', buffering=True) as f:
            # 使用for循环遍历文件对象
            for line in f:
                #print(line, end='')
                list=line.split("=")
                if "resourcePath" == list[0]:
                    self.fold_address = list[1]

        print(self.fold_address.strip(" ,\r\n"))
        print(batname)

    def executebat(self):
        os.chdir(self.fold_address.strip(" ,\r\n"))
        p = Popen("cmd.exe /c  start "+self.exebatname, shell=False)