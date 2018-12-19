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

for n in range (2,20):
    print ('Creating VLAN' + str(n))
    config_commands = ['vlan' + str (n), "name" + str(n)]
    output = net_connect.send_config_set (config_commands)
    print (output)

#test
#output = net_connect.send_config_set("int loop 0", "ip address 1.1.1.1 255.255.255.0")
