import socket

# ================== CONFIGURAÇÃO ==================
TCP_IP = '127.0.0.1'
TCP_PORTA = 5005
# =================================================

try:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((TCP_IP, TCP_PORTA))

    print("✅ Conectado ao servidor!")
    print("w = cima | s = baixo | a = esquerda | d = direita | quit = sair")

    while True:
        msg = input("Comando: ").strip()
        
        if not msg:
            continue

        cliente.send(msg.encode('utf-8'))

        if msg.lower() in ['quit', 'q']:
            break

except ConnectionRefusedError:
    print("❌ ERRO: servidor não está rodando!")

except Exception as e:
    print(f"Erro: {e}")

finally:
    try:
        cliente.close()
    except:
        pass

    print("Conexão encerrada.")
