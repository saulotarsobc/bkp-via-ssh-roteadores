import paramiko
from config import address, port, username, password

command = "display current-configuration | no-more"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password, port=port)

(stdin, stdout, stderr) = ssh.exec_command(command)

stdin.close()

for line in stdout.readlines():
    if line:
        print(line.replace('\r\n', ''))
