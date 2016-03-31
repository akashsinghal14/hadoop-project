#!/usr/bin/python2

import os,allip
import getpass
import commands
import thread

def hdfs(folder,k):
		commands.getoutput("sshpass -p redhat ssh -o StrictHostKeyChecking=no %s  mkdir /%s ;  mkdir -p /root/Desktop/hadoop/{datanode,namenode}"%(k,folder))
		nn = open('/root/Desktop/hadoop/namenode/hdfs-site.xml','w')
		nn.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/%s</value>
</property>
</configuration>
'''%folder)
		nn.close()
		commands.getoutput("scp /root/Desktop/hadoop/namenode/hdfs-site.xml  root@%s:/etc/hadoop/"%k)

def core(k):
		nc = open('/root/Desktop/hadoop/namenode/core-site.xml','w')
		nc.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>
'''%k)
		nc.close()
		commands.getoutput("scp /root/Desktop/hadoop/namenode/core-site.xml  root@%s:/etc/hadoop/"%k)

def mapred(k):
		nj = open('/root/Desktop/hadoop/namenode/mapred-site.xml','w')
		nj.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>%s:9002</value>
</property>

</configuration>
'''%k)
		nj.close()
		commands.getoutput("scp /root/Desktop/hadoop/namenode/mapred-site.xml  root@%s:/etc/hadoop/"%k)

def namenode(k):
	#print "hello"
	#print k
	#folder=raw_input("enter the directory name: ")
	os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter the directory name'  8 40   2>/tmp/foldername.txt")
	os.system("dialog --infobox 'processing please wait...' 3 34")
	f19=open("/tmp/foldername.txt")
	folder=f19.read()
	f19.close()
	hdfs(folder,k)
	core(k)	
	mapred(k)

def chooseip():
	os.system("dialog --infobox 'processing please wait...' 3 34")
	allip.all_ip()
	os.system("dialog --infobox 'processing please wait...' 3 34")
	#ii=commands.getoutput('nmap -sP  192.168.137.0/24 | grep 192 |  cut  -d: -f 2 | cut -c 22-36 > /root/Desktop/hup.txt')
	ip_master = commands.getoutput('ifconfig eth0 | grep 192 | cut -d: -f 2 | cut -c 1-11')
	ii=commands.getoutput('nmap -n -sP  %s.0/24 --exclude %s.1,%s.2,%s.254 | grep 192 |  cut  -d: -f 2 | cut -c 22-36  > /root/Desktop/hup.txt'%(ip_master,ip_master,ip_master,ip_master))
	f=open("/root/Desktop/hup.txt")
	ii=f.read()
	f.close()
	iilist = ii.split('\n')
	#i=raw_input("enter a s.no. to make that ip namenode: ")
	#i=int(i)
	os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter a s.no'  8 40   2>/tmp/snon.txt")
	f20=open("/tmp/snon.txt")
	d=f20.read()
	f20.close()
	i=d
	i=int(i)
	#print i
	#print iilist[i]
	k = iilist[i]
	#print k
	namenode(k)

def chooseipstart():
	os.system("dialog --infobox 'processing please wait...' 3 34")
	#allip.all_ip()
	os.system("dialog --infobox 'processing please wait...' 3 34")
	ip_master = commands.getoutput('ifconfig eth0 | grep 192 | cut -d: -f 2 | cut -c 1-11')
	ii=commands.getoutput('nmap -n -sP  %s.0/24 --exclude %s.1,%s.2,%s.254 | grep 192 |  cut  -d: -f 2 | cut -c 22-36  > /root/Desktop/hup.txt'%(ip_master,ip_master,ip_master,ip_master))
	#ii=commands.getoutput('nmap -sP  192.168.137.0/24 | grep 192 |  cut  -d: -f 2 | cut -c 22-36 > /root/Desktop/hup.txt')
	f=open("/root/Desktop/hup.txt")
	ii=f.read()
	f.close()
	iilist = ii.split('\n')
	#i=raw_input("enter a s.no. to format,start namenode and jobtracker to that ip namenode: ")
	#i=int(i)
	#os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter a s.no'  5 40   2>/tmp/snon.txt")
	f20=open("/tmp/snon.txt")
	d=f20.read()
	f20.close()
	i=d
	i=int(i)
	#print i
	#print iilist[i]
	k = iilist[i]
	#print k
	start(k)
	

def start(k):
	os.system("dialog --infobox 'processing please wait...' 3 34")
	os.system("ssh %s iptables -F > /dev/null"%k)
	os.system("ssh %s setenforce 0 > /dev/null"%k)
	os.system("ssh %s service iptables save > /dev/null"%k)
	os.system("ssh %s echo Y | hadoop namenode -format  > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh stop namenode > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh start namenode > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh stop jobtracker > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh start jobtracker > /dev/null"%k)
	
	
