import socket
import pygame
import threading

# ================== CONFIG ==================
TCP_IP = '127.0.0.1'
TCP_PORTA = 5005
BUFFER = 1024
# ============================================

x = 375
y = 275
speed = 15

lock = threading.Lock()  # 🔥 proteção contra conflito

# ================== CLIENTE ==================
def handle_client(conn, addr):
    global x, y
    print(f"✅ Cliente conectado: {addr}")

    try:
        while True:
            data = conn.recv(BUFFER)
            if not data:
                break

            command = data.decode().strip().lower()
            print("Comando:", command)

            with lock:  # 🔥 protege x e y
                if command == 'w':
                    y -= speed
                elif command == 's':
                    y += speed
                elif command == 'a':
                    x -= speed
                elif command == 'd':
                    x += speed
                elif command in ['q', 'quit']:
                    break

                x = max(0, min(750, x))
                y = max(0, min(550, y))

    except Exception as e:
        print("Erro cliente:", e)

    finally:
        conn.close()
        print("❌ Cliente desconectado")

# ================== SERVIDOR ==================
def iniciar_servidor():
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((TCP_IP, TCP_PORTA))
        servidor.listen()

        print(f"🚀 Servidor rodando em {TCP_IP}:{TCP_PORTA}")

        while True:
            conn, addr = servidor.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

    except Exception as e:
        print("❌ ERRO SERVIDOR:", e)

threading.Thread(target=iniciar_servidor, daemon=True).start()

# ================== PYGAME ==================
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

print("🟦 Pygame rodando...")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # 🔥 leitura protegida
    with lock:
        pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
