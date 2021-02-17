#!/usr/bin/env python
import os 
import subprocess   
from subprocess import check_call
from scapy.all import *
import sys, signal 
from multiprocessing import Process
import time
import csv
import pandas as pd




if os.path.exists('output.txt'):
  os.remove('output.txt')

if os.path.exists('myOutput-01.csv'):
  os.remove('myOutput-01.csv')
#interface adını 9-17. satırlarda alıyoruz
os.system('airmon-ng >> output.txt')
f = open('output.txt', 'r')
i = 0
for line in f:
  for word in line.split():
    i+=1
    if i == 6:
      interface = word
      print(interface)
order = "airmon-ng start {} && airmon-ng check kill".format(interface)
geny  = os.system(order)
os.system('airmon-ng >> output2.txt')
f = open('output2.txt', 'r')
i = 0
for line in f:
  for word in line.split():
    i+=1
    if i == 6:
      interfacemon = word
      print(interfacemon)


order = f"airodump-ng {interfacemon} -M -w myOutput --output-format csv & sleep 20; kill $!"
geny = os.system(order)
print("****************1***************************")
in_file = pd.read_csv("input.csv")
inputCSV = in_file.copy()
print("****************5***************************")
in_file1= pd.read_csv("myOutput-01.csv",sep=r'\s*,\s*',header=0, engine='python')
outputCSV= in_file1.copy()
print("****************6***************************")
inBSSID = list(inputCSV["BSSID"])
outBSSID = list(outputCSV["BSSID"])
print("******************2*************************")
print("list len ",len(outBSSID))
print("*******************3************************")
for item in outBSSID:
    if item in inBSSID:
        filter = outputCSV["BSSID"]==item
        ch = int(outputCSV[filter]["channel"])
        print(item + ": ",ch)
        print("***************4****************************")
    else: 
      print(item," : bulunamadi")
