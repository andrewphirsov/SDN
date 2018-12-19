from netmiko import ConnectHandler



ios_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.100.100.100',
    'username':'admin',
    'password':'cisco'
}

net_connect = ConnectHandler(**ios_l2)
output = net_connect.send_command ('show ip int brief')
print (output)
config_commands = ["hostname PY_SWITCH","int loop 0","ip address 1.1.1.1 255.255.255.0"]
output = net_connect.send_config_set (config_commands)
print (output)

fvlan=2
lvlan=20
print ('Creating VLANs' + str(fvlan) + "to" + str(lvlan))
for n in range (2,20):
    config_commands = ['vlan ' + str (n), "name " + str(n)]
    print ('.')
    #output = net_connect.send_config_set (config_commands)
    net_connect.send_config_set (config_commands)
    #print (output)
print ('VLANs' + str(fvlan) + "to" + str(lvlan) + "created")

#test
#output = net_connect.send_config_set("int loop 0", "ip address 1.1.1.1 255.255.255.0")
