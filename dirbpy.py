#!/usr/bin/python

import socket;
import requests;
import sys;


tgtHost = sys.argv[1]
pathToDirList = sys.argv[2]

"""
connect_ex((host,port))
"""
def dirchecker(listOfPaths):
	try:
		response_code = requests.get('http://' + tgtHost + '/' + listOfPaths).status_code
	except Exception:
		sys.exit(1)
	if(response_code == 200):
		print "\nhttp://%s/%s  : FOUND" %(tgtHost, listOfPaths)


hostsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""The error indicator is 0 if the operation succeeded, otherwise the value of the errno variable."""
try:	
	#strTgtHost = "http://www." + str(tgtHost) + ".com:80"
	status = hostsocket.connect_ex((tgtHost,80))
	hostsocket.close()
	if (status == 0):
		print "\n==Connection tested...OK=="
		pass
	else:
		print "\n===Cannot reach specified host %s===" %(tgthost)
		sys.exit(1)
	
except socket.error:
	print "\nexception for connect_ex to %s" %(tgtHost)
	sys.exit(1)

print "\nImporting your wordlist..this might take a second"
try:
	with open(pathToDirList) as file:
		import_list = file.read().strip().split('\n')
except IOError:
	print "\n couldn't import"
	sys.exit(1)

for i in range(len(import_list)):
	dirchecker(import_list[i])
print "\ncomplete"

