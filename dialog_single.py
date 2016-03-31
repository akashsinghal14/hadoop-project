#!/usr/bin/python2

import os,time,sys
import getpass
import commands
import thread

#os.system("dialog --infobox 'Welcome TO my hadoop project' 7 30")
os.system("dialog --backtitle 'HADOOP' --title 'WELCOME' --infobox 'Welcome To My Hadoop Project.' 10 30")
time.sleep(1.0)
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

				os.system("dialog --backtitle 'HADOOP' --title 'MENU' --menu 'select a option' 12 50 4 1 'create single node cluster' 2 'start all services' 3 'stop all services' 4  'Go back to main menu' 2>/tmp/menu.txt")
				m=open("/tmp/menu.txt")
				ch=m.read()
				m.close()
				#print type(ch)
				if ch=="1":
					import single_node
					single_node.chooseip()
				elif ch=="2":
					import single_node
					single_node.s_all()
					
				elif ch=="3":
					import single_node
					single_node.s_all1()
				
				elif ch=="4":
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
