#!/usr/bin/python2

import os,sys
import getpass
import commands
import thread
import random

def hdfs(k,folder1,folder2):
		os.system("sshpass -p redhat ssh -o StrictHostKeyChecking=no %s mkdir -p /root/Desktop/singlenode"%k)
		nn = open('/root/Desktop/singlenode/hdfs-site.xml','w')
		nn.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/%s</value>
</property>

<property>
<name>dfs.data.dir</name>
<value>/%s</value>
</property>
</configuration>
'''%(folder1,folder2))
		nn.close()
		commands.getoutput("cp /root/Desktop/singlenode/hdfs-site.xml  /etc/hadoop/")

def core(k):
		nc = open('/root/Desktop/singlenode/core-site.xml','w')
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
		commands.getoutput("cp /root/Desktop/singlenode/core-site.xml  /etc/hadoop/")

def mapred(k):
		nj = open('/root/Desktop/singlenode/mapred-site.xml','w')
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
		commands.getoutput("cp /root/Desktop/singlenode/mapred-site.xml  /etc/hadoop/")

def ins_jdk(k):
	os.system("ssh %s yum install jdk -y"%k)

def ins_hadoop(k):
	os.system("ssh %s yum install hadoop -y"%k)


def singlenode(k):
	folder1=random.randint(000,999)
	folder2=random.randint(000,999)
	commands.getoutput("ssh %s  mkdir /%s ; mkdir /%s"%(k,folder1,folder2))
	hdfs(k,folder1,folder2)
	core(k)	
	mapred(k)


def chooseip():
	k='127.0.0.1'
	#thread.start_new_thread(ins_jdk, (k,))
	#thread.start_new_thread(ins_hadoop, (k,))
	os.system("mkdir -p /root/Desktop/singlenode  > /dev/null")
	singlenode(k)
	chooseipstart()

def chooseipstart():
	k='127.0.0.1'
	start(k)
	

def start(k):
	os.system("ssh %s yum install hadoop jdk -y  > /dev/null"%k)
	os.system("dialog --infobox 'processing please wait...' 3 34")	
	os.system("ssh %s iptables -F > /dev/null"%k)
	os.system("ssh %s setenforce 0 > /dev/null"%k)
	os.system("ssh %s service iptables save > /dev/null"%k)
	os.system("ssh %s echo Y | hadoop namenode -format  > /dev/null"%k)
	os.system("dialog --infobox 'processing please wait...' 3 34")	
	os.system("ssh %s hadoop-daemon.sh stop namenode > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh start namenode > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh stop jobtracker > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh start jobtracker > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh stop datanode > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh start datanode > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh stop tasktracker > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh start tasktracker > /dev/null"%k)

def startall(k):
	os.system("ssh %s chmod +x /usr/sbin/stop-all.sh"%k)
	os.system("ssh %s chmod +x /usr/sbin/stop-mapred.sh"%k)
	os.system("ssh %s chmod +x /usr/sbin/stop-dfs.sh"%k)
	os.system("ssh %s chmod +x /usr/sbin/slaves.sh"%k)
	os.system("ssh %s start-all.sh"%k)
def stopall(k):
	os.system("ssh %s chmod +x /usr/sbin/start-all.sh"%k)
	os.system("ssh %s chmod +x /usr/sbin/start-mapred.sh"%k)
	os.system("ssh %s chmod +x /usr/sbin/start-dfs.sh"%k)
	os.system("ssh %s chmod +x /usr/sbin/slaves.sh"%k)
	os.system("ssh %s stop-all.sh"%k)

def s_all():
	k='127.0.0.1'
	startall(k)

def s_all1():
	k='127.0.0.1'
	stopall(k)

	
