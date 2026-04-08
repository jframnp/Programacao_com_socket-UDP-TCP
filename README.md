# Controle Remoto de Objeto via Socket TCP + Pygame

**Atividade: Análise de Programação de Socket UDP e TCP**  
**Disciplina:** Redes de Computadores  
**Professor:** Dr. Bruno da Silva Rodrigues  
**Alunos:** João Francisco RA:10443666
            Gabriel Messora RA:
            Luis Felipe RA:

# Questão 3
## Descrição do Projeto
Aplicação de **controle remoto de objeto** usando socket **TCP** e biblioteca **Pygame**.  

O servidor abre uma janela gráfica (Pygame) com um quadrado azul.  
O cliente (console) envia comandos em tempo real (WASD) para mover o quadrado.  
Foi utilizada **thread** para separar a recepção de comandos do loop gráfico do Pygame.

**Por que TCP?**  
Garante entrega confiável e na ordem correta dos comandos (diferente do UDP).

**Atende 100% aos critérios do enunciado:**
- Não é transferência simples de arquivos
- Não é jogo da velha
- Não é quiz
- Usa Pygame + socket + thread

## Como Executar

### Requisitos
- Python 3.8+
- Biblioteca Pygame: `pip install pygame`

### Passo a passo
1. Abra **dois terminais/IDLE** (ou dois computadores).
2. No primeiro terminal execute o servidor:
   ```bash
   python ServerRemoteControl.py
