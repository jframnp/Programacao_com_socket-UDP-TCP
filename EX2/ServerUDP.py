import socket

IP = "127.0.0.1"
PORTA = 10438

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORTA))

print("Servidor rodando...")

while True:
    data, addr = sock.recvfrom(1024)
    mensagem = data.decode()

    print(f"Cliente: {mensagem}")

    if mensagem.upper() == "QUIT":
        print("Encerrando servidor...")
        break

    resposta = input("Você: ")
    sock.sendto(resposta.encode(), addr)

    if resposta.upper() == "QUIT":
        print("Encerrando servidor...")
        break

sock.close()
