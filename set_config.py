from netmiko import ConnectHandler

ssh_client = ConnectHandler(

    device_type = 'cisco_ios',
    host = '192.168.0.19',
    port = 22,
    username = 'cisco',
    password = 'cisco123!',

)

config_commands = [
    'int loopback 1',
    'ip addres 2.2.2.1 255.255.255.0',
    'description Este es la interfaz de loopback configurada con un script en python'
]

output = ssh_client.send_config_set(config_commands)
print("Cconfig output from the devvice:\n{}\n".format(output))
