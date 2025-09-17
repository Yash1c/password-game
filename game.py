import time

def animacao_carregamento(texto, duracao=1.5):
    print(texto, end="", flush=True)
    for _ in range(3):
        time.sleep(duracao/6)
        print(".", end="", flush=True)
    time.sleep(duracao/6)
    print()

def inicio():
    print("==================================")
    print("Bem vindo ao jogo da senha !!!")
    print("==================================")
    print("O objetivo do jogo é você digitar a senha")
    print("conforme as regras que forem passando")
    print("EXEMPLO:\nA senha tem 3 letras e 2 números\nSENHA ATUAL: ABC23")
    print("==================================\n")
    
    while True:
        print("Está pronto para começar?")
        print("1 - Sim")
        print("2 - Não")
        resposta = input("Resposta: ")
        if resposta == "1":
            print("==================================\n")
            animacao_carregamento("Iniciando jogo")
            função1()
            break
        elif resposta == "2":
            print("==================================\n")
            print("Tudo bem, até a próxima !!!")
            print("==================================\n")
            exit()
        else:
            print("==================================\n")
            print("Resposta inválida, tente novamente !!!")
            print("==================================\n")

def função1():
    while True:
        print("==================================")
        print("REGRA 1: A senha deve ter exatamente 6 caracteres")    
        senha = str(input("Digite a senha: "))
        print(f"Senha digitada: {senha}")

        if len(senha) != 6:
            print("⚠️ Ops!!! A senha deve ter exatamente 6 caracteres.")
            print("==================================\n")
            continue
        else:
            print(f"Senha atual: {senha}")
            print("==================================\n")
            time.sleep(1)
            função2(senha)
            break

def função2(senha_anterior):
    while True:
        print("==================================")
        print("REGRA 2: Agora a senha deve ter pelo menos 2 LETRAS")
        print(f"SENHA ATUAL: {senha_anterior}")
        nova_senha = str(input("Digite a nova senha: "))
        print(f"Senha digitada: {nova_senha}")

        # Verifica se mantém a regra anterior
        if len(nova_senha) != 6:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 6 caracteres.")
            print("==================================\n")
            continue
        
        # Verifica a nova regra
        letras = sum(1 for char in nova_senha if char.isalpha())
        if letras < 2:
            print("⚠️ Ops!!! A senha deve ter pelo menos 2 letras.")
            print("==================================\n")
            continue
        else:
            print(f"Senha atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            função3(nova_senha)
            break

def função3(senha_anterior):
    while True:
        print("==================================")
        print("REGRA 3: Agora a senha deve ter pelo menos 2 NÚMEROS")
        print(f"SENHA ATUAL: {senha_anterior}")
        nova_senha = str(input("Digite a nova senha: "))
        print(f"Senha digitada: {nova_senha}")

        # Verifica regras anteriores
        if len(nova_senha) != 6:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 6 caracteres.")
            print("==================================\n")
            continue
        
        letras = sum(1 for char in nova_senha if char.isalpha())
        if letras < 2:
            print("⚠️ Ops!!! A senha ainda deve ter pelo menos 2 letras.")
            print("==================================\n")
            continue
        
        # Verifica a nova regra
        numeros = sum(1 for char in nova_senha if char.isdigit())
        if numeros < 2:
            print("⚠️ Ops!!! A senha deve ter pelo menos 2 números.")
            print("==================================\n")
            continue
        else:
            print(f"Senha atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            função4(nova_senha)
            break

def função4(senha_anterior):
    while True:
        print("==================================")
        print("REGRA 4: Agora a senha deve começar com uma LETRA MAIÚSCULA")
        print(f"SENHA ATUAL: {senha_anterior}")
        nova_senha = str(input("Digite a nova senha: "))
        print(f"Senha digitada: {nova_senha}")

        # Verifica regras anteriores
        if len(nova_senha) != 6:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 6 caracteres.")
            print("==================================\n")
            continue
        
        letras = sum(1 for char in nova_senha if char.isalpha())
        if letras < 2:
            print("⚠️ Ops!!! A senha ainda deve ter pelo menos 2 letras.")
            print("==================================\n")
            continue
        
        numeros = sum(1 for char in nova_senha if char.isdigit())
        if numeros < 2:
            print("⚠️ Ops!!! A senha ainda deve ter pelo menos 2 números.")
            print("==================================\n")
            continue
        
        # Verifica a nova regra
        if not nova_senha[0].isupper():
            print("⚠️ Ops!!! A senha deve começar com uma letra maiúscula.")
            print("==================================\n")
            continue
        else:
            print(f"Senha atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            função5(nova_senha)
            break

def função5(senha_anterior):
    while True:
        print("==================================")
        print("REGRA 5: Agora a senha deve terminar com um NÚMERO")
        print(f"SENHA ATUAL: {senha_anterior}")
        nova_senha = str(input("Digite a nova senha: "))
        print(f"Senha digitada: {nova_senha}")

        # Verifica regras anteriores
        if len(nova_senha) != 6:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 6 caracteres.")
            print("==================================\n")
            continue
        
        letras = sum(1 for char in nova_senha if char.isalpha())
        if letras < 2:
            print("⚠️ Ops!!! A senha ainda deve ter pelo menos 2 letras.")
            print("==================================\n")
            continue
        
        numeros = sum(1 for char in nova_senha if char.isdigit())
        if numeros < 2:
            print("⚠️ Ops!!! A senha ainda deve ter pelo menos 2 números.")
            print("==================================\n")
            continue
        
        if not nova_senha[0].isupper():
            print("⚠️ Ops!!! A senha ainda deve começar com uma letra maiúscula.")
            print("==================================\n")
            continue
        
        # Verifica a nova regra
        if not nova_senha[-1].isdigit():
            print("⚠️ Ops!!! A senha deve terminar com um número.")
            print("==================================\n")
            continue
        else:
            print(f"Senha atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            função6(nova_senha)
            break

def função6(senha_anterior):
    while True:
        print("==================================")
        print("DESAFIO FINAL: Agora a senha deve conter pelo menos um símbolo especial (!@#$%&*)")
        print(f"SENHA ATUAL: {senha_anterior}")
        nova_senha = str(input("Digite a nova senha: "))
        print(f"Senha digitada: {nova_senha}")

        # Verifica regras anteriores
        if len(nova_senha) != 6:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 6 caracteres.")
            print("==================================\n")
            continue
        
        letras = sum(1 for char in nova_senha if char.isalpha())
        if letras < 2:
            print("⚠️ Ops!!! A senha ainda deve ter pelo menos 2 letras.")
            print("==================================\n")
            continue
        
        numeros = sum(1 for char in nova_senha if char.isdigit())
        if numeros < 2:
            print("⚠️ Ops!!! A senha ainda deve ter pelo menos 2 números.")
            print("==================================\n")
            continue
        
        if not nova_senha[0].isupper():
            print("⚠️ Ops!!! A senha ainda deve começar com uma letra maiúscula.")
            print("==================================\n")
            continue
        
        if not nova_senha[-1].isdigit():
            print("⚠️ Ops!!! A senha ainda deve terminar com um número.")
            print("==================================\n")
            continue
        
        # Verifica a nova regra
        simbolos_especiais = "!@#$%&*"
        tem_simbolo = any(char in simbolos_especiais for char in nova_senha)
        if not tem_simbolo:
            print("⚠️ Ops!!! A senha deve conter pelo menos um símbolo especial (!@#$%&*).")
            print("==================================\n")
            continue
        else:
            print(f"Senha atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            vitoria(nova_senha)
            break

def vitoria(senha_final):
    print("==================================")
    animacao_carregamento("Verificando senha")
    print("==================================")
    print("PARABÉNS! Você conseguiu criar uma senha segura!")
    print(f"SENHA FINAL: {senha_final}")
    print("==================================\n")
    
    while True:
        print("Deseja jogar novamente?")
        print("1 - Sim")
        print("2 - Não")
        resposta = input("Resposta: ")
        if resposta == "1":
            print("==================================\n")
            animacao_carregamento("Reiniciando jogo")
            inicio()
            break
        elif resposta == "2":
            print("==================================\n")
            print("Obrigado por jogar! Até a próxima!")
            print("==================================\n")
            exit()
        else:
            print("==================================\n")
            print("Resposta inválida, tente novamente!")
            print("==================================\n")

# Inicia o jogo
inicio()