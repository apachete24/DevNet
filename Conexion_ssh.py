from netmiko import ConnectHandler

ssh_client = ConnectHandler(

    device__type = 'cisco_ios',
    host = '192.168.0.18',
    port = 22,
    username = 'cisco',
    password = 'cisco123',

)
# enviaar ejecutar unos comando simples y mostrar lo que devuelve

output = ssh_client.send_command("show ip int brief")
print("IP interface status and configuration:\n{}\n".format(output))

