from ncclient import manager
from pathlib import Path
import xmltodict
dataFolder=Path(r"C:\Data\Python\SDN\SDN\on-box\configs\base")

netconf_filter = open(dataFolder/'request.xml').read()

if __name__=="__main__":
    with manager.connect(host="10.100.100.120",port="22",username="admin",password="cisco",hostkey_verify=False) as m:
        print ("Here are netconf capabilities of this switch:")
        for capabilitity in m.server_capabilities:
            print (capabilitity)
        print(netconf_filter)