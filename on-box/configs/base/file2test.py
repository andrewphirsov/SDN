from datetime import datetime
from pathlib import Path
from pprint import pprint
dataFolder=Path(r"C:\Data\Python\SDN\SDN\on-box\configs\base")
logfile=dataFolder/'example.log'
def readlog(log):
    with open(log,"r") as f:
        print (f.read())

def writelog(log, name):
    print("Writing shit to file...")
    logtime=str(datetime.now())
    with open(log,"a") as f:
        f.writelines ("entry loged at %s by %s" %(logtime,name) + "\n" )

if __name__ == "__main__":
    name=input('What is your name?\n')
    print ("Adding new log entry")
    writelog(logfile,name)
    print('')
    print('LogFile now contains:')
    print('--------------------')
    readlog(logfile)