#!/usr/bin/env python
import os
import subprocess
from subprocess import check_call

if os.path.exists('output.txt'):
  os.remove('output.txt')
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
order = f"airodump-ng {interfacemon} -M >> scan.txt & sleep 2; kill $!"
geny = os.system(order)
#geny  = os.system("airodump-ng wlan0mon -M & sleep 20; kill $!")
#with open("scan.txt", "w", encoding="utf-8") as filetxt:
  #filetxt.write(geny)
#cmd = os.system("sleep 15")
#os.system('{} >> scan.txt'.format(order))




