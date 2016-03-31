#!/usr/bin/python2

import os
import getpass
import commands
import thread

def all_ip():
	file_ip1=open("/tmp/allip.txt","w")
	file_ip1.write('''available ip and totsl ram and hard disk is:-\n\ns.no.		ip		ram	free space\n\n''')
	file_ip1.close()
	#print "you are connected to this ip's"
	ip_master = commands.getoutput('ifconfig eth0 | grep 192 | cut -d: -f 2 | cut -c 1-11')
	ipl=commands.getoutput('nmap -n -sP  %s.0/24 --exclude %s.1,%s.2,%s.254 | grep 192 |  cut  -d: -f 2 | cut -c 22-36'%(ip_master,ip_master,ip_master,ip_master))
	iplist = ipl.split('\n')
	#print "S.No.\t","     ip's \t\ttotal ava ram\t\t free hard disk"
	s=0
	for i in iplist:
		#print "and available ram and memory is"
		if i=='192.168.183.1' or i=='192.168.183.2' or i=='192.168.183.254':
			continue
		y=commands.getoutput("sshpass -p redhat ssh -o StrictHostKeyChecking=no %s  free -m | grep Mem | cut -d: -f 2 | cut -c 34-36; df -h | grep sda2 | awk '{print $4}'"%i)
		ylist=y.split('\n')
		os.system("exit")
		file_ip=open("/tmp/allip.txt","a")
		file_ip.write('''%s	%s		%s	%s\n'''%(s,i,ylist[0],ylist[1]))
		file_ip.close()
		#print "",s,"\t",i,"\t    ",ylist[0],"mb","\t\t    ",ylist[1]
		s+=1
#	os.system("dialog --checklist 'select an ip to which you wana make namenode:' 40 40 4 %s+=1 %s off"%(s,iplist[s]))
	os.system("dialog --textbox /tmp/allip.txt  12 50")	
