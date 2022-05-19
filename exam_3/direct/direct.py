import requests
import html
import argparse
import os
import re
list = []
def getlist():
    f = open("list.txt","r")
    for x in f:
        list.append(x.replace("\n",""))
    print(list)
    f.close()
def getinfo():
    for i in range(len(list)):
        url = "http://192.168.11.128/uploads/viewimg.php?name={}".format(list[i])
        res = requests.get(url)
        x = str(list[i]).replace("/","%2F")
        f = open("data/{}.txt".format(x),"w")
        f.write(res.text)
        f.close()
if __name__ == '__main__':
    getlist()
    getinfo()