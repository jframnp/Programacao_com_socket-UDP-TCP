import socket

IP = "127.0.0.1"
PORTA = 10438

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente iniciado...")

while True:
    mensagem = input("Você: ")
    sock.sendto(mensagem.encode(), (IP, PORTA))

    if mensagem.upper() == "QUIT":
        print("Encerrando cliente...")
        break

    data, addr = sock.recvfrom(1024)
    resposta = data.decode()

    print(f"Servidor: {resposta}")

    if resposta.upper() == "QUIT":
        print("Encerrando cliente...")
        break

sock.close()
