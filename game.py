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
        print("REGRA 1: A senha deve ter exatamente 8 caracteres")    
        senha = str(input("Digite a senha: "))
        print(f"Senha digitada: {senha}")

        if len(senha) != 8:
            print("⚠️ Ops!!! A senha deve ter exatamente 8 caracteres.")
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
        if len(nova_senha) !=8:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 8 caracteres.")
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
        if len(nova_senha) != 8:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 8 caracteres.")
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
        if len(nova_senha) != 8:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 8 caracteres.")
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
        if len(nova_senha) != 8:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 8 caracteres.")
            print("==================================\n")
            continue
        
        letras = sum(1 for char in nova_senha if char.isalpha())
        if letras < 2:
            print("⚠️ Ops!!! A senha ainda deve ter pelo menos 8 letras.")
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
        print("REGRA 6: Agora a senha deve conter pelo menos um símbolo especial (!@#$%&*)")
        print(f"SENHA ATUAL: {senha_anterior}")
        nova_senha = str(input("Digite a nova senha: "))
        print(f"Senha digitada: {nova_senha}")

        # Verifica regras anteriores
        if len(nova_senha) != 8:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 8 caracteres.")
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
            função7(nova_senha)
            break

def função7(senha_anterior):
    while True:
        print("==================================")
        print("REGRA 7: Agora a senha não pode ter cacteres repetidos consecutivos\n(ex:“aa” ou “11”).")
        print(f"SENHA ATUAL: {senha_anterior}")
        nova_senha = str(input("Digite a nova senha: "))
        print(f"Senha digitada: {nova_senha}")

        # Verifica regras anteriores
        if len(nova_senha) != 8:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 8 caracteres.")
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

        simbolos_especiais = "!@#$%&*"
        tem_simbolo = any(char in simbolos_especiais for char in nova_senha)
        if not tem_simbolo:
            print("⚠️ Ops!!! A senha deve conter pelo menos um símbolo especial (!@#$%&*).")
            print("==================================\n")
            continue

        # Verificar a nova regra
        tem_repetido = False
        for i in range(len(nova_senha) - 1):
            if nova_senha[i] == nova_senha[i + 1]:
                tem_repetido = True
                break

        if tem_repetido:
            print("⚠️ Ops!!! A senha não pode ter caracteres repetidos consecutivos.")
            print("==================================\n")
            continue
        else:
            print(f"Senha atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            função8(nova_senha)
            break



def função8(senha_anterior):
    while True:
        print("==================================")
        print("REGRA 8: Agora a senha deve conter pelo menos um caractere acentuado\n(á, é, í, ó, ú, ç, â, ê, ô, ã, õ, etc.)")
        print(f"SENHA ATUAL: {senha_anterior}")
        nova_senha = str(input("Digite a nova senha: "))
        print(f"Senha digitada: {nova_senha}")

        # Verifica regras anteriores
        if len(nova_senha) != 8:
            print("⚠️ Ops!!! A senha ainda deve ter exatamente 8 caracteres.")
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

        simbolos_especiais = "!@#$%&*"
        tem_simbolo = any(char in simbolos_especiais for char in nova_senha)
        if not tem_simbolo:
            print("⚠️ Ops!!! A senha deve conter pelo menos um símbolo especial (!@#$%&*).")
            print("==================================\n")
            continue

        tem_repetido = False
        for i in range(len(nova_senha) - 1):
            if nova_senha[i] == nova_senha[i + 1]:
                tem_repetido = True
                break
        if tem_repetido:
            print("⚠️ Ops!!! A senha não pode ter caracteres repetidos consecutivos.")
            print("==================================\n")
            continue

        # Verifica se tem acento
        acentuados = "áéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ"
        tem_acentuado = any(char in acentuados for char in nova_senha)
        if not tem_acentuado:
            print("⚠️ Ops!!! A senha deve conter pelo menos um caractere acentuado.")
            print("==================================\n")
            continue
        else:
            print(f"Senha atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            função9(nova_senha)
            break
        
# Função 9: Números romanos
# Função 9: Números romanos
def função9(senha_anterior):
    while True:
        print("==================================")
        print("REGRA 9: Digite dois números romanos (I, II, III, IV, V, VI, VII, VIII, IX, X) que multiplicados resultem em 15.")
        print(f"SENHA ATUAL: {senha_anterior}")
        # Verifica todas as regras anteriores
        numeros = sum(1 for char in senha_anterior if char.isdigit())
        if numeros < 2:
            print("⚠️ Ops!!! A senha deve ter pelo menos 2 números.")
            print("==================================\n")
            continue
        if not senha_anterior[0].isupper():
            print("⚠️ Ops!!! A senha deve começar com uma letra maiúscula.")
            print("==================================\n")   
            continue
        if not senha_anterior[-1].isdigit():
            print("⚠️ Ops!!! A senha deve terminar com um número.")
            print("==================================\n")
            continue
        simbolos_especiais = "!@#$%&*"
        tem_simbolo = any(char in simbolos_especiais for char in senha_anterior)
        if not tem_simbolo:
            print("⚠️ Ops!!! A senha deve conter pelo menos um símbolo especial (!@#$%&*).")
            print("==================================\n")
            continue
        tem_repetido = False
        for i in range(len(senha_anterior) - 1):
            if senha_anterior[i] == senha_anterior[i + 1]:
                tem_repetido = True
                break
        if tem_repetido:
            print("⚠️ Ops!!! A senha não pode ter caracteres repetidos consecutivos.")
            print("==================================\n")
            continue
        acentuados = "áéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ"
        tem_acentuado = any(char in acentuados for char in senha_anterior)
        if not tem_acentuado:
            print("⚠️ Ops!!! A senha deve conter pelo menos um caractere acentuado.")
            print("==================================\n")
            continue

        # Regra dos romanos - CORREÇÃO
        romanos = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
        
        # Extrai apenas os números romanos da entrada (remove a senha atual)
        entrada1 = input("Digite o primeiro número romano: ").upper().strip()
        entrada2 = input("Digite o segundo número romano: ").upper().strip()
        
        # Remove a senha atual se o usuário digitou ela junto
        if senha_anterior in entrada1:
            entrada1 = entrada1.replace(senha_anterior, "").strip()
        if senha_anterior in entrada2:
            entrada2 = entrada2.replace(senha_anterior, "").strip()
        
        # Remove quaisquer números ou caracteres especiais que não sejam romanos
        # Mantém apenas letras I, V, X
        entrada1 = ''.join([c for c in entrada1 if c in 'IVX']).strip()
        entrada2 = ''.join([c for c in entrada2 if c in 'IVX']).strip()
        
        if not entrada1 or not entrada2:
            print("⚠️ Ops!!! Digite apenas números romanos válidos (I, II, III, IV, V, VI, VII, VIII, IX, X).")
            print("==================================\n")
            continue
        
        if entrada1 not in romanos or entrada2 not in romanos:
            print("⚠️ Ops!!! Digite apenas números romanos válidos (I, II, III, IV, V, VI, VII, VIII, IX, X).")
            print("==================================\n")
            continue
        
        resultado = romanos[entrada1] * romanos[entrada2]
        if resultado != 15:
            print(f"⚠️ Ops!!! {entrada1} x {entrada2} = {resultado}. O resultado deve ser 15.")
            print("==================================\n")
            continue
        else:
            print(f"Correto! {entrada1} x {entrada2} = 15")
            print("==================================\n")
            nova_senha = senha_anterior + entrada1 + entrada2
            print(f"Senha atual: {nova_senha}")
            time.sleep(1)
            função_final(nova_senha)
            break

# Função final: Underscore no meio
def função_final(senha_anterior):
    while True:
        print("==================================")
        print("REGRA FINAL: A senha deve conter um '_' exatamente no meio")
        print(f"SENHA ATUAL: {senha_anterior}")
        nova_senha = str(input("Digite a senha final: "))
        print(f"Senha digitada: {nova_senha}")
        # Verifica todas as regras anteriores
        numeros = sum(1 for char in nova_senha if char.isdigit())
        if numeros < 2:
            print("⚠️ Ops!!! A senha deve ter pelo menos 2 números.")
            print("==================================\n")
            continue
        if not nova_senha[0].isupper():
            print("⚠️ Ops!!! A senha deve começar com uma letra maiúscula.")
            print("==================================\n")
            continue
        if not nova_senha[-1].isdigit():
            print("⚠️ Ops!!! A senha deve terminar com um número.")
            print("==================================\n")
            continue
        simbolos_especiais = "!@#$%&*"
        tem_simbolo = any(char in simbolos_especiais for char in nova_senha)
        if not tem_simbolo:
            print("⚠️ Ops!!! A senha deve conter pelo menos um símbolo especial (!@#$%&*).")
            print("==================================\n")
            continue
        tem_repetido = False
        for i in range(len(nova_senha) - 1):
            if nova_senha[i] == nova_senha[i + 1]:
                tem_repetido = True
                break
        if tem_repetido:
            print("⚠️ Ops!!! A senha não pode ter caracteres repetidos consecutivos.")
            print("==================================\n")
            continue
        acentuados = "áéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ"
        tem_acentuado = any(char in acentuados for char in nova_senha)
        if not tem_acentuado:
            print("⚠️ Ops!!! A senha deve conter pelo menos um caractere acentuado.")
            print("==================================\n")
            continue

        meio = len(nova_senha) // 2
        if nova_senha[meio] != '_':
            print("⚠️ Ops!!! O caractere '_' deve estar exatamente no meio!")
            print("==================================\n")
            continue
        else:
            print(f"Senha final: {nova_senha}")
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