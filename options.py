#!/usr/bin/python2

import os,time,sys
import getpass
import commands
import thread

def options():
	while True:
		os.system("dialog --backtitle 'HADOOP' --title 'MENU' --menu 'select a option' 12 50 4 1 'Setup customize hadoop' 2 'Setup minimal hadoop/sudo cluster' 3 'Setup typical hadoop' 4 'To exit properly' 2>/tmp/options.txt")
		#ch=raw_input("Enter ur choice : ")
		m=open("/tmp/options.txt")
		ch=m.read()
		m.close()
		if ch=="1":
			import dialog
			dialog.login()

		elif ch=="2":
			import dialog_single
			dialog_single.login()
		elif ch=="3":
			import typ_inst
			typ_inst.login()
		elif ch=="4":
			q=os.system("dialog  --backtitle 'HADOOP' --title 'WARNING' --yesno  'are you sure  Y/N'  5 40")
			if q==0:
				#import options
				#options.options()
				exit()
			else:
				continue

		
		elif ch=="":
			q=os.system("dialog  --backtitle 'HADOOP' --title 'WARNING' --yesno  'are you sure  Y/N'  5 40")
			if q==0:
				#import options
				#options.options()
				exit()
			else:
				continue

		else:
			print "not supported"
options()
