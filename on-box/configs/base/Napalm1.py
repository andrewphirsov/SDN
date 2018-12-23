import json
from napalm import get_network_driver
driver=get_network_driver('ios')
iosvl2=driver('10.100.100.100','admin','cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print (json.dumps(ios_output,indent=4))
ios_output = iosvl2.get_interfaces()
print (json.dumps(ios_output,indent=4))
ios_output = iosvl2.get_interfaces_counters()
print (json.dumps(ios_output,indent=4))