import paramiko
import sys

if len(sys.argv) != 6:
    exit('script <ip> <porta_ssh> <user> <pass> <huawei|mikrotik]>')

address = sys.argv[1]
port = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
marca = sys.argv[5]

if marca == 'mikrotik':
    comando = "export"
    nome = f'{address}.rsc'
    
elif marca == "huawei":
    comando = "display current-configuration | no-more"
    

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=address, username=username, password=password, port=port)
    (stdin, stdout, stderr) = ssh.exec_command(comando)
    stdin.close()
    
    with open(nome, "a") as file_object:
        for  linha in stdout.readlines():
            lin = linha.replace('\r\n', '')
            file_object.write(f'{lin}\n')
    
except Exception as e:
    print(f'Erro >>> : {e}')