import paramiko

address = '172.33.255.2'
port = 22
username = 'root'
password = '10l15p130A@'

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password, port=port)
(stdin, stdout, stderr) = ssh.exec_command(command)
# stdin.close()
""" for line in stdout.readlines():
    print(line) """

print(stdout.readlines())
