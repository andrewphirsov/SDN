#import socket
#def getRemoteMachineInfo():
 #   remote_host='www.myhost.com'
   ## try:
      #  print ("IP address of %s: %s" % (remote_host,socket.gethostbyname(remote_host)))
   # except socket.error as err_msg:
   #     print ("%s: %s" %(remote_host, err_msg))
#if __name__ == "__main__":
   # getRemoteMachineInfo()
print ("variable equal: %s" % (__name__))
if (__name__ == "__main__"):
    print ("This is only for MAIN")
else:
    print ("This is for Imported")