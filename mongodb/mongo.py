#!/usr/bin/python3

import sys
from pymongo import MongoClient

host = "172.16.10.13"
port = "31251"

client = MongoClient("mongodb://"+str(host)+":"+str(port))
db=client.admin

num = len(sys.argv)
if num == 2:
  serverStatusResult=db.command("serverStatus")[sys.argv[1]]
elif num == 3:
  serverStatusResult=db.command("serverStatus")[sys.argv[1]][sys.argv[2]]
elif num == 4:
  serverStatusResult=db.command("serverStatus")[sys.argv[1]][sys.argv[2]][sys.argv[3]]
elif num == 5:
  serverStatusResult=db.command("serverStatus")[sys.argv[1]][sys.argv[2]][sys.argv[3]][sys.argv[4]]
elif num == 6:
  serverStatusResult=db.command("serverStatus")[sys.argv[1]][sys.argv[2]][sys.argv[3]][sys.argv[4]][sys.argv[5]]

print(serverStatusResult)

