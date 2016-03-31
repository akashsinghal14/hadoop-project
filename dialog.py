#!/usr/bin/python2

import os,time,sys,allip,namenode,datanode
import getpass
import commands
import thread

#os.system("dialog --infobox 'Welcome TO my hadoop project' 7 30")
os.system("dialog --backtitle 'HADOOP' --title 'WELCOME' --infobox 'Welcome To My Hadoop Project.' 10 30")
time.sleep(0.1)
def login():
	u=os.system("dialog --backtitle 'HADOOP' --title 'USERNAME' --inputbox 'enter your username' 7 30   2>/tmp/username.txt")
	p=os.system("dialog --backtitle 'HADOOP' --title 'PASSWORD' --insecure --passwordbox 'enter your password' 7 30   2>/tmp/password.txt")
	f=open("/tmp/username.txt")
	u=f.read()
	f.close()
	f1=open("/tmp/password.txt")
	p=f1.read()
	f1.close()

	if u=="":
		if p=="":
			while True:

				os.system("dialog --backtitle 'HADOOP' --title 'MENU' --menu 'select a option' 25 60 17 1 'create namenode and jobtracker' 2 'format, start namenode and jobtracker' 3 'create datanode and tasktracker' 4 'start datanode and tasktracker' 5 'HIVE (use this option when a cluster is ready)' 6 'use PIG (when a cluster is ready)'  7 'set high priority to a job' 8 'make a client' 9 'Decommision nodes' 10 'commision nodes' 11 'hbase' 12 'create hdfs users' 13 'set quota on space' 14 'set qouta on file' 15 'setup fair scheduler'  16 'upload a file' 17 'Go back to main menu'  2>/tmp/menu.txt")
				m=open("/tmp/menu.txt")
				ch=m.read()
				m.close()
				#print type(ch)
				if ch=="1":
					#allip.all_ip()
					namenode.chooseip()
					#namenode()
				elif ch=="2":
					namenode.chooseipstart()
				elif ch=="3":
					datanode.chooseip1()
				elif ch=="4":
					datanode.chooseipstart1()

				elif ch=="5":			
					datanode.hive()
				elif ch=="6":			
					datanode.pig()
	
				elif ch=="7":
					datanode.priority()
		
				elif ch=="8":
					datanode.client()

				elif ch=="9":
					os.system("dialog --infobox 'processing please wait...' 3 34")
					ii=commands.getoutput('nmap -sP  192.168.137.0/24 | grep 192 |  cut  -d: -f 2 | cut -c 22-36 > /root/Desktop/hup.txt')
					f=open("/root/Desktop/hup.txt")
					ii=f.read()
					f.close()
					iilist = ii.split('\n')
					f20=open("/tmp/snon.txt")
					d=f20.read()
					f20.close()
					i=d
					i=int(i)
					k = iilist[i]
					name=k
					allip.all_ip()
					os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter ips to make that exclude from cluster'  8 60   2>/tmp/decomm.txt")
					f20=open("/tmp/decomm.txt")
					d=f20.read()
					f20.close()
					dlist = d.split()
					deco=d
					datanode.decomm(name,deco)

				elif ch=="10":
					os.system("dialog --infobox 'processing please wait...' 3 34")
					ii=commands.getoutput('nmap -sP  192.168.137.0/24 | grep 192 |  cut  -d: -f 2 | cut -c 22-36 > /root/Desktop/hup.txt')
					f=open("/root/Desktop/hup.txt")
					ii=f.read()
					f.close()
					iilist = ii.split('\n')
					f20=open("/tmp/snon.txt")
					d=f20.read()
					f20.close()
					i=d
					i=int(i)
					k = iilist[i]
					name=k
					allip.all_ip()
					os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter ips to make that include from cluster'  8 60   2>/tmp/comm.txt")
					f20=open("/tmp/comm.txt")
					d=f20.read()
					f20.close()
					dlist = d.split()
					co=d
					datanode.comm(name,co)
					#datanode.comm()
					
				elif ch=="11":
					datanode.hbase()	

				elif ch=="12":
					datanode.users()

				elif ch=="13":
					datanode.spacequota()

				elif ch=="14":
					datanode.filequota()
			
				elif ch=="15":
					datanode.fairsch()			

				elif ch=="16":
					datanode.uploadfiles()			



				elif ch=="17":
					#os.system("dialog --backtitle 'HADOOP' --title 'WARNING' --inputbox  'are you sure  Y/N'  5 40   2>/tmp/decision.txt")
					#f2=open("/tmp/decision.txt")
					#d=f2.read()
					#f2.close()
					#if d=="y" or d=="Y" or d=="yes" or d=="YES" or d=="Yes":
					q=os.system("dialog  --backtitle 'HADOOP' --title 'WARNING' --yesno  'are you sure  Y/N'  5 40")
					if q==0:
						import options
						options.options()
						#exit()
					else:
						continue
				elif ch=="":
					q=os.system("dialog  --backtitle 'HADOOP' --title 'WARNING' --yesno  'are you sure  Y/N'  5 40")
					if q==0:
						import options
						options.options()
						#exit()
					else:
						continue
					
			else:
				print "wrong choice"
		else:
			os.system("dialog --msgbox 'password is incorrect' 7 30")
			login()
	else:
		os.system("dialog --msgbox 'username is incorrect' 7 30")
		login()

login()	
