# Edited version on mongodb template for Zabbix
Netkiller shell script replaced with python script, because in new linux like Ubunutu
Bionic cant install mongo shell version 3.6 and later.

Installation
-----------
1. Install depencies:
```
apt install python3 python3-pymongo
```
2. Install files:
```
cp mongo.py /usr/local/bin
chmod a+x /usr/local/bin/mongo.py
cp userparameter_mongodb.conf /etc/zabbix/zabbix_agent.d/
```
3. Import mongodb_templates.xml in zabbix frontend


# Original Credit for Netkiller 
Zabbix Plugin

Donations
---------
http://www.netkiller.cn/home/donations.html
