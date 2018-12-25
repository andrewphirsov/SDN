'''
import socket
def getRemoteMachineInfo():
    remote_host='www.myhost.com'
    try:
        print ("IP address of %s: %s" % (remote_host,socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print ("%s: %s" %(remote_host, err_msg))
if __name__ == "__main__":
    getRemoteMachineInfo()

def getStrangeIpFormat():
   text='Strange format of ip'
   normalIP=socket.gethostbyname('www.myhost.com')
   preStrangeIP=socket.inet_aton(normalIP)
   print (text.capitalize() + "%s: %s" %(normalIP,preStrangeIP))
   print ("Length of string is: %s" %(len(text)))
   print ("First symbol of text is: " + text[0])
   username=input('What is your name?')
   print ('Hello, ' + username + '!')
   mylist =['snow','sun',3,18,18.5]
   secondlist = ['rain','moon']
   print (mylist[1])
   print(type(mylist[1]))
   mylist.extend (secondlist)
   print (mylist)
   notlist=mylist.copy()
   print (notlist)
getStrangeIpFormat()


i=1
while (i<=100):
   print (i+i)
   i=i+1
print ("Done")

for letter in 'Santa Claws':
   print(letter)
'''
from paramiko import _winapi
from pathlib import Path
dataFolder=Path(r"C:\Data\Python\SDN\SDN\on-box\configs\base")
employee_file = open(dataFolder/'Employees.txt','r')
print (employee_file.readlines())
for employee in employee_file.readlines():
   print(employee)
employee_file.close

employee_file = open(dataFolder/'Employees1.txt','w')
employee_file.write('\nBob - NiceJerk')
employee_file.close