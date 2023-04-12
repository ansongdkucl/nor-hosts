
import paramiko
import subprocess
import os

ip = '10.36.50.60'
un = os.environ['USER']
pw = os.environ['PASSWORD']
#secret = os.environ['secret']



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port=22, username=un,password=pw,allow_agent=False,look_for_keys=False)
cmd1 = ("cd /mnt/hosts; grep ^172.17. hosts | awk '{{print $2}}'")

stdin, stdout, stderr = ssh.exec_command(cmd1)
ok = stdout.readlines()
#print(ok)
new_lst = [x[:-1] for x in ok]
print(new_lst)

print(new_lst, file=open("/home/dansong/scripts/auto-vlan/inventory/ host_list.py","w"))



