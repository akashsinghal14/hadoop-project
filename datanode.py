#!/usr/bin/python2

import os,allip,random
import getpass
import commands
import thread

def hdfs(q):
		#commands.getoutput("sshpass -p redhat ssh -o StrictHostKeyChecking=no %s  mkdir /datanode"%k)
		nn = open('/root/Desktop/hadoop/datanode/hdfs-site.xml','w')
		nn.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/datanode</value>
</property>
</configuration>
''')
		nn.close()
		#commands.getoutput("scp /root/Desktop/hadoop/datanode/hdfs-site.xml  root@%s:/etc/hadoop/"%k)

def core(q):
		nc = open('/root/Desktop/hadoop/datanode/core-site.xml','w')
		nc.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>
'''%q)
		nc.close()
		#commands.getoutput("scp /root/Desktop/hadoop/datanode/core-site.xml  root@%s:/etc/hadoop/"%k)

def mapred(q):
		nj = open('/root/Desktop/hadoop/datanode/mapred-site.xml','w')
		nj.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>%s:9002</value>
</property>

</configuration>
'''%q)
		nj.close()
		#commands.getoutput("scp /root/Desktop/hadoop/datanode/mapred-site.xml  root@%s:/etc/hadoop/"%k)
def copy(k):
	os.system("ssh %s  rm -rf /datanode  > /dev/null"%k)
	os.system("ssh %s  mkdir /datanode  > /dev/null"%k)
	os.system("scp /root/Desktop/hadoop/datanode/hdfs-site.xml  root@%s:/etc/hadoop/    > /dev/null"%k)
	os.system("scp /root/Desktop/hadoop/datanode/core-site.xml  root@%s:/etc/hadoop/   > /dev/null"%k)
	os.system("scp /root/Desktop/hadoop/datanode/mapred-site.xml  root@%s:/etc/hadoop/   > /dev/null"%k)

def datanode(q):
	#os.system("dialog --infobox 'processing please wait...' 3 34")
	#print "hello"
	#print k
	#folder=raw_input("enter the directory name: ")
	#os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter the directory name'  5 40   2>/tmp/foldername.txt")
	#os.system("dialog --infobox 'processing please wait...' 3 34")
	#f19=open("/tmp/foldername.txt")
	#folder=random.randint(000,999)
	#commands.getoutput("ssh %s  mkdir /%s"%(k,folder))
	#f19.close()
	thread.start_new_thread(hdfs,(q,))
	thread.start_new_thread(core,(q,))	
	thread.start_new_thread(mapred,(q,))

def chooseip1():
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
	f21=open("/tmp/snon.txt")
	n=f21.read()
	f21.close()
	l=n
	l=int(l)
	q = iilist[l]
	os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter a s.no to make that ip datanode follow by space'  8 40   2>/tmp/snod.txt")
	f20=open("/tmp/snod.txt")
	d=f20.read()
	f20.close()
	#i=d
	#i=int(i)
	#print i
	#print iilist[i]
	#k = iilist[i]
	dlist = d.split()
	datanode(q)
	for z in dlist:
		#print "hello hi i am here did you miss me"
		z=int(z)
		k=iilist[z]
		thread.start_new_thread(copy,(k,))

def chooseipstart1():
	os.system("dialog --infobox 'processing please wait...' 3 34")
	#allip.all_ip()
	os.system("dialog --infobox 'processing please wait...' 3 34")
	#ii=commands.getoutput('nmap -sP  192.168.137.0/24 | grep 192 |  cut  -d: -f 2 | cut -c 22-36 > /root/Desktop/hup.txt')
	ip_master = commands.getoutput('ifconfig eth0 | grep 192 | cut -d: -f 2 | cut -c 1-11')
	ii=commands.getoutput('nmap -n -sP  %s.0/24 --exclude %s.1,%s.2,%s.254 | grep 192 |  cut  -d: -f 2 | cut -c 22-36  > /root/Desktop/hup.txt'%(ip_master,ip_master,ip_master,ip_master))
	f=open("/root/Desktop/hup.txt")
	ii=f.read()
	f.close()
	iilist = ii.split('\n')
	#i=raw_input("enter a s.no. to format,start namenode and jobtracker to that ip namenode: ")
	#i=int(i)
	#os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter a s.no to make that ip datanode follow by space'  8 40   2>/tmp/snod.txt")
	f20=open("/tmp/snod.txt")
	d=f20.read()
	f20.close()
	#i=d
	#i=int(i)
	#print i
	#print iilist[i]
	#k = iilist[i]
	#print k
	dlist = d.split()
	for z in dlist:
		z=int(z)
		k=iilist[z]
		thread.start_new_thread(start,(k,))

	#start(k)
	

def start(k):
	#os.system("dialog --infobox 'processing please wait...' 3 34")
	os.system("ssh %s iptables -F  > /dev/null"%k)
	os.system("ssh %s setenforce 0 > /dev/null"%k)
	os.system("ssh %s service iptables save  > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh stop datanode > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh start datanode > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh stop tasktracker > /dev/null"%k)
	os.system("ssh %s hadoop-daemon.sh start tasktracker > /dev/null"%k)
	


#hive should be on client

def hive():
	os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter client ip'  8 40   2>/tmp/hive_client.txt ")
	f20=open("/tmp/hive_client.txt")
	d=f20.read()
	f20.close()
	os.system("ssh %s tar -xzvf /root/Desktop/hadoop_project_files/framework/apache-hive-0.13.1-bin.tar.gz"%d)
	os.system("ssh %s mv apache-hive-0.13.1-bin  /hive"%d)
	h = open('/root/.bashrc','a')
	h.write('''
export HIVE_HOME=/hive/
export PATH=/hive/bin:$PATH
''')
	h.close()


#pig should be on client

def pig():
	os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter client ip'  8 40   2>/tmp/pig_client.txt ")
	f20=open("/tmp/pig_client.txt")
	d=f20.read()
	f20.close()
	os.system("ssh %s tar -xzvf /root/Desktop/hadoop_project_files/framework/pig-0.12.1.tar.gz"%d)
	os.system("ssh %s mv pig-0.12.1  /pig"%d)
	p = open('/root/.bashrc','a')
	p.write('''
export PIG_HOME=/pig/
export PATH=/pig/bin:$PATH
''')
	p.close()	
	
	
#hbase 
def hbase():
	os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter client ip'  8 40   2>/tmp/hbase_client.txt ")
	f20=open("/tmp/hbase_client.txt")
	d=f20.read()
	f20.close()
	os.system("ssh %s tar -xzvf /root/Desktop/hadoop_project_files/framework/hbase-0.98.9-hadoop1-bin.tar.gz"%d)
	os.system("ssh %s mv hbase-0.98.9-hadoop1  /hbase"%d)
	p = open('/root/.bashrc','a')
	p.write('''
export HBASE_HOME=/hbase/
export PATH=/hbase/bin:$PATH
''')
	p.close()
	os.system("start-hbase.sh")
	os.system("hbase shell")

#setting priority

def priority():
	#q=commands.getoutput('hadoop job -list > /tmp/priority.txt')
	qq=commands.getoutput("hadoop job -list all | grep job_ | awk {'print$1'}")
	#os.system("dialog --textbox /tmp/jobsid.txt  16 50")
	qqlist=qq.split('\n')
	#print qqlist
	s=1
	for i in qqlist:
		#print i
		os.system("dialog --checklist 'Choose a jobid to set high priority:' 10 60 2  '%s' '%s' off   2> /tmp/priority.txt"%(i,i))
	f=open("/tmp/priority.txt")
	a=f.read()
	f.close()
	print type(a)
	os.system("hadoop job -set-priority %s VERY_HIGH"%a)
	#	z=["%s %s off"%(s,i)]
	#	print z[0]
	#	s+=1
	#k=0
	#for j in qqlist:
	#	os.system("dialog --checklist 'choose a jobid to set high priority:' 10 100 '%s' 1 '%s' off  2> /tmp/priority.txt"%(s,z[0]))

#making client

def client():
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
	f22=open("/tmp/snon.txt")
	x=f22.read()
	f22.close()
	v=x
	v=int(v)
	p = iilist[v]
	os.system("dialog --backtitle 'HADOOP'  --inputbox  'enter a s.no to make that ip client'  8 40   2>/tmp/client_ip.txt")
	f21=open("/tmp/client_ip.txt")
	c=f21.read()
	f21.close()
	l=c
	l=int(l)
	q = iilist[l]
	os.system("ssh %s yum install hadoop jdk -y"%q)
	os.system("mkdir  /root/Desktop/client")
	c=open('/root/Desktop/client/core-site.xml','w')
	c.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>
'''%p)
	c.close()
	os.system("scp /root/Desktop/client/core-site.xml  root@%s:/etc/hadoop/   > /dev/null"%q)
	
#decommision nodes
def decomm(name,*deco):
	
	
	os.system('scp root@%s:/etc/hadoop/hdfs-site.xml /root/Desktop/hadoop/  > /dev/null'%name)
	f=open("/root/Desktop/hadoop/hdfs-site.xml",'r')
	de=f.read()
	de=de.replace('</configuration>','''<property>  
<name>dfs.hosts.exclude</name>
<value>/etc/hadoop/excludes</value>
</property>
</configuration>''')#replace </config> with new property
	f.close()
	f=open("/root/Desktop/hadoop/hdfs-site.xml",'w')
	f.write(de)
	f.close()
	f=open("/root/Desktop/hadoop/excludes",'w')
	f.write(*deco)
	f.close()
	x=os.system('scp /root/Desktop/hadoop/{hdfs-site.xml,excludes} root@%s:/etc/hadoop/  > /dev/null'%name)
	if x==0:
		os.system('ssh %s hadoop dfsadmin -refreshNodes  > /dev/null'%name)
		#print "nodes decomissioned"
		#os.system('rm -f /root/Desktop/{hdfs-site.xml,excludes}')
		#os.system('chmod +x /usr/sbin/start-balancer.sh')#balancer permission execute
		#os.system('chmod +x /usr/sbin/stop-balancer.sh')
		#os.system('start-balancer.sh')
	else:
		print "error copying files to namenode"
		print "nodes decomissioning failed"	

#commision nodes

def comm(name,*co):
	os.system('scp root@%s:/etc/hadoop/hdfs-site.xml /root/Desktop/hadoop/  > /dev/null'%name)
	f=open("/root/Desktop/hadoop/hdfs-site.xml",'r')
	de=f.read()
	de=de.replace('</configuration>','''<property>  
<name>dfs.hosts</name>
<value>/etc/hadoop/includes</value>
</property>
</configuration>''')#replace </config> with new property
	f.close()
	f=open("/root/Desktop/hadoop/hdfs-site.xml",'w')
	f.write(de)
	f.close()
	f=open("/root/Desktop/hadoop/includes",'w')
	f.write(*co)
	f.close()
	x=os.system('scp /root/Desktop/hadoop/{hdfs-site.xml,includes} root@%s:/etc/hadoop/  > /dev/null'%name)
	if x==0:
		os.system('ssh %s hadoop dfsadmin -refreshNodes  > /dev/null'%name)
		#print "nodes decomissioned"
		#os.system('rm -f /root/Desktop/{hdfs-site.xml,excludes}')
		#os.system('chmod +x /usr/sbin/start-balancer.sh')#balancer permission execute
		#os.system('chmod +x /usr/sbin/stop-balancer.sh')
		#os.system('start-balancer.sh')
	else:
		print "error copying files to namenode"
		print "nodes decomissioning failed"	

#make user

def users():
	os.system("dialog --infobox 'processing please wait...' 3 34")
	os.system("hadoop fs -mkdir /user")
	os.system("hadoop fs -chmod 777 /user")
	os.system("dialog  --inputbox  'enter username'  5 40   2>/tmp/hdfsuser.txt")
	os.system("dialog --infobox 'processing please wait...' 3 34")
	f20=open("/tmp/hdfsuser.txt")
	d=f20.read()
	f20.close()
	os.system("hadoop fs -mkdir /user/%s"%d)

#set space quota

def spacequota():
	os.system("dialog  --inputbox  'enter a username to set quota on space'  8 60   2>/tmp/userspacequota.txt")
	f25=open("/tmp/userspacequota.txt")
	u=f25.read()
	f25.close()
	os.system("dialog  --inputbox  'enter space quota in mb'  8 60   2>/tmp/spacequota.txt")
	os.system("dialog --infobox 'processing please wait...' 3 34")
	f20=open("/tmp/spacequota.txt")
	d=f20.read()
	f20.close()
	i=int(d)
	i=i*1024*1024
	os.system("hadoop dfsadmin -setSpaceQuota %s  /user/%s"%(i,u))
	

#set quota on files
def filequota():
	os.system("dialog  --inputbox  'enter a username to set quota on files'  8 60   2>/tmp/userfilequota.txt")
	f25=open("/tmp/userfilequota.txt")
	u=f25.read()
	f25.close()
	os.system("dialog  --inputbox  'enter total no of files which user can upload' 8 60 2>/tmp/filequota.txt")
	os.system("dialog --infobox 'processing please wait...' 3 34")
	f20=open("/tmp/filequota.txt")
	d=f20.read()
	f20.close()
	i=int(d)
	os.system("hadoop dfsadmin -setSpaceQuota %s  /user/%s"%(i,u))


#setup fair scheduler
def fairsch():
	#os.system("dialog --infobox 'processing please wait...' 3 34")
	#allip.all_ip()
	#os.system("dialog --infobox 'processing please wait...' 3 34")
	'''ip_master = commands.getoutput('ifconfig eth0 | grep 192 | cut -d: -f 2 | cut -c 1-11')
	ii=commands.getoutput('nmap -n -sP  %s.0/24 --exclude %s.1,%s.2,%s.254 | grep 192 |  cut  -d: -f 2 | cut -c 22-36  > /root/Desktop/hup.txt'%(ip_master,ip_master,ip_master,ip_master))
	f=open("/root/Desktop/hup.txt")
	ii=f.read()
	f.close()
	iilist = ii.split('\n')
	#i=raw_input("enter a s.no. to make that ip namenode: ")
	#i=int(i)
	f21=open("/tmp/snon.txt")
	n=f21.read()
	f21.close()
	l=n
	l=int(l)'''
	q ="127.0.0.1"
	
	os.system('scp root@%s:/etc/hadoop/mapred-site.xml /root/Desktop/hadoop/  > /dev/null'%q)
	f=open("/root/Desktop/hadoop/mapred-site.xml",'r')
	fa=f.read()
	fa=fa.replace('</configuration>','''<property>  
<name>mapred.job.tracker.taskscheduler</name>
<value>arg.apache.hadoop.mapred.fairscheduler</value>
</property>
</configuration>''')#replace </config> with new property
	f.close()
	f=open("/root/Desktop/hadoop/mapred-site.xml",'w')
	f.write(fa)
	f.close()
	os.system('scp /root/Desktop/hadoop/mapred-site.xml root@%s:/etc/hadoop/'%q)
	os.system("ssh %s hadoop-daemon.sh stop jobtracker > /dev/null"%q)
	os.system("ssh %s hadoop-daemon.sh start jobtracker > /dev/null"%q)



#uploadfiles

def uploadfiles():
	os.system("dialog  --inputbox  'enter path of file you want to upload'  8 60   2>/tmp/uploadfiles.txt")
	f=open("/tmp/uploadfiles.txt",'r')
	up=f.read()
	f.close()
	os.system("hadoop fs -put %s /"%up)
	
