import paramiko
import threading
import time

hostname = '172.33.255.2'
port = 22
username = 'root'
password = '10l15p130A@'

comando = '''
echo 1
echo 2
echo 3
echo 4
echo 5
'''

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username,
                password=password, port=port)

    # print(ssh)
    # time.sleep(2)

    (stdin, stdout, stderr) = ssh.exec_command(comando)
    stdin.close()

    dados = stdout.readlines()

    for i in dados:
        print(i.replace('\n', ''))

except Exception as e:
    print(f'Erro >>> : {e}')
