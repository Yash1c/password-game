import time 
import os
import string
import random # Para regra 7
from collections import Counter # Para regra 10

# Uma função de animação (nada importante. . .)
def animacao_carregamento(texto, duracao):
    print(texto, end="", flush=True)
    for _ in range(3):
        time.sleep(duracao/6)
        print(".", end="", flush=True)
    time.sleep(duracao/6)
    print()

# Limpa a tela do terminal (Linux/macOS: clear, Windows: cls)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------------------------------------------------------------
# FUNÇÃO PRINCIPAL PARA VERIFICAR REGRAS ANTERIORES
# --------------------------------------------------------------------------------

def verificar_regras_anteriores(senha: str, ate_regra: int) -> bool:
    """
    Verifica todas as regras anteriores até a regra especificada.
    Retorna True se todas as regras forem atendidas, False caso contrário.
    """
    # Regra 1: Tamanho mínimo de 10 caracteres
    if len(senha) < 10:
        print("⚠️  A senha deve ter 10 ou mais caracteres, esqueceu? >:(")
        return False
    
    # Regra 2: Pelo menos 1 letra e 1 número
    tem_letras = any(char.isalpha() for char in senha)
    tem_numeros = any(char.isdigit() for char in senha)
    if not (tem_letras and tem_numeros):
        print("⚠️ Ops!!! A senha deve conter pelo menos 1 número e 1 letra!")
        return False
    
    # Regra 3: Pelo menos 1 letra maiúscula
    if ate_regra >= 3 and not any(char.isupper() for char in senha):
        print("⚠️ A senha deve conter pelo menos 1 letra MAIÚSCULA!")
        return False
    
    # Regra 4: Pelo menos 1 caractere especial
    if ate_regra >= 4 and not any(char in string.punctuation for char in senha):
        print("⚠️ A senha deve conter pelo menos 1 caractere especial (ex: !@#$%)!")
        return False
    
    # Regra 5: Soma dos dígitos igual a 25
    if ate_regra >= 5:
        soma = sum(int(c) for c in senha if c.isdigit())
        if soma != 25:
            print(f"⚠️ A soma dos dígitos deve ser 25 (atualmente: {soma}).")
            return False
    
    # Regra 6: Conter número romano entre I e X
    if ate_regra >= 6 and not contem_numero_romano(senha):
        print("⚠️ A senha deve conter um número romano válido entre I e X (ex: IV, VI, X).")
        return False
    
    # Regra 7: Número aleatório (precisa ser passado separadamente)
    # Esta regra é tratada dentro da função regra7 pois precisa do número gerado
    
    # Regra 8: Palíndromo de 3+ caracteres
    if ate_regra >= 8 and not tem_palindromo_3_chars(senha):
        print("⚠️ A senha deve conter um palíndromo de 3+ letras (ex: 'ana', 'radar')!")
        return False
    
    # Regra 9: Sequência crescente de 3 dígitos
    if ate_regra >= 9 and not tem_sequencia_crescente(senha):
        print("⚠️ A senha deve conter 3 dígitos em sequência crescente (ex: '123', '456')!")
        return False
    
    # Regra 10: Anagrama de 2024 ou 2025
    if ate_regra >= 10 and not tem_anagrama_ano(senha):
        print("⚠️ A senha deve conter um anagrama de '2024' ou '2025'!")
        return False
    
    # Regra 11: Soma dos dígitos primos igual a 13
    if ate_regra >= 11 and not soma_digitos_primos_igual_13(senha):
        digitos_primos = [c for c in senha if c.isdigit() and eh_primo(int(c))]
        soma_atual = sum(int(d) for d in digitos_primos)
        print(f"⚠️ A soma dos dígitos primos (2,3,5,7) deve ser 13 (atual: {soma_atual})!")
        return False
    
    return True

# --------------------------------------------------------------------------------
# FUNÇÕES DAS REGRAS ESPECÍFICAS
# --------------------------------------------------------------------------------

# Função da regra 5
def soma_digitos_igual_25(texto: str) -> bool:
    """Retorna True se a soma de todos os dígitos numéricos no texto for exatamente 25."""
    return sum(int(c) for c in texto if c.isdigit()) == 25

# Função da regra 6 - Tokens válidos de números romanos entre I e X
ROMAN_TOKENS = [
    "X", "IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"
]
def contem_numero_romano(texto: str) -> bool:
    """Retorna True se o texto contiver ao menos um número romano entre I e X."""
    t = texto.upper()
    return any(token in t for token in ROMAN_TOKENS)

# Função da regra 8 
def tem_palindromo_3_chars(texto: str) -> bool:
    """Retorna True se a senha contiver um palíndromo de pelo menos 3 letras CONTÍGUAS."""
    n = len(texto)
    for L in range(3, n + 1):
        for i in range(0, n - L + 1):
            sub = texto[i:i+L]
            if all(c.isalpha() for c in sub):
                s = sub.lower()
                if s == s[::-1]:
                    return True
    return False

# Função da regra 9
def tem_sequencia_crescente(texto: str) -> bool:
    """Retorna True se houver 3 dígitos consecutivos na string formando sequência crescente (ex: '123')."""
    n = len(texto)
    for i in range(n - 2):
        a, b, c = texto[i:i+3]
        if a.isdigit() and b.isdigit() and c.isdigit():
            if int(a) + 1 == int(b) and int(b) + 1 == int(c):
                return True
    return False

# Função da regra 10
def tem_anagrama_ano(texto: str) -> bool:
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    # Verifica blocos contíguos de 4 dígitos na string original
    for i in range(len(texto) - 3):
        segmento = texto[i:i+4]
        if all(ch.isdigit() for ch in segmento):
            if is_anagram(segmento, "2024") or is_anagram(segmento, "2025"):
                return True
    return False

# Função da regra 11
def eh_primo(n: int) -> bool:
    """Retorna True se o número é primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def soma_digitos_primos_igual_13(texto: str) -> bool:
    """Retorna True se a soma dos dígitos primos for 13."""
    primos = [int(c) for c in texto if c.isdigit() and eh_primo(int(c))]
    return sum(primos) == 13

# Função da regra 12
def eh_senha_perfeita(texto: str) -> bool:
    """Verifica se a senha atende a um critério final especial."""
    # Deve ter pelo menos uma letra de cada vogal
    vogais = {'a', 'e', 'i', 'o', 'u'}
    texto_lower = texto.lower()
    tem_todas_vogais = all(vogal in texto_lower for vogal in vogais)
    
    # Deve ter um padrão simétrico de caracteres especiais
    especiais = [c for c in texto if c in string.punctuation]
    eh_simetrico = especiais == especiais[::-1] if especiais else False
    
    return tem_todas_vogais and eh_simetrico

# --------------------------------------------------------------------------------
# FUNÇÕES DO JOGO
# --------------------------------------------------------------------------------

# Função para iniciar o jogo
def inicio_jogo():
    print("================================")
    print("Bem vindo ao jogo da senha!!!")
    print("")
    print("O objetivo do jogo é você digitar a senha\nconforme as regras que forem passando.")
    print("EXEMPLO:\nA senha DEVE ter 3 letras e 2 números\nSENHA DIGITADA: ABC23")
    print("================================")

# Loop essencial para inicio de tela do jogo
    while True:
        print("Está pronto para começar?")
        print("1 - Sim? >;D\n2 - Não ;(")
        print("")
        resposta = input("Resposta: ")
        if resposta == "1":
            print("================================")
            animacao_carregamento("Iniciando jogo", 4)
            regra1()
            break # Quebra o loop 
        elif resposta == "2":
            print("================================")
            print("Opa tudo bem, até a próxima!!!")
            exit()
        else:
            print("================================")
            print("Eita, talvez você digitou algo errado, tente novamente!")
            print("================================")

# Primeira regrinha do jogo
def regra1():
    limpar_tela()
    print("================================")
    
    primeira_tentativa = True # Variável para controlar se é a primeira vez que o usuário erra

    while True:
        print("")
        senha = str(input("Digite qualquer senha: "))
        print("")
        print(f"Senha digitada: {senha}")

        if len(senha) >= 10:
            # Senha válida, segue para a próxima regra
            print("================================\n")
            time.sleep(1)
            regra2(senha)
            break
        else:
            # Senha inválida
            if primeira_tentativa:
                # Mensagem especial na primeira vez que o usuário erra
                print("\nOpa, esqueci de avisar >;)")
                print("A senha deve ter 10 ou mais caracteres...")
                primeira_tentativa = False # Marca que a primeira chance "engraçada" passou
            else:
                # Mensagem mais direta nas tentativas seguintes
                print("⚠️  A senha deve ter 10 ou mais caracteres, esqueceu? >:(")
            
            print("================================")

# Segunda regra e assim sucessivamente. . .
def regra2(senha_anterior):
    limpar_tela()
    print("Boa!")
    animacao_carregamento("Agora a próxima regra", 4)
    print("================================\n")
    print(f"Senha anterior: {senha_anterior}\n")

    while True:
        print("2º Regra: A senha deve ter letras e números!\n")
        nova_senha = str(input("Digite sua senha: "))
        print("")
        print(f"Senha digitada: {nova_senha}")
        
        # Verificando a 1º regra anterior. . .
        if len(nova_senha) < 10:
            print("⚠️  A senha deve ter 10 ou mais caracteres, esqueceu? >:(")
            print("==================================\n")
            continue
            
        numeros = sum(1 for char in nova_senha if char.isdigit())
        letras = sum(1 for char in nova_senha if char.isalpha())
        if numeros < 1 or letras < 1:
            print("⚠️ Ops!!! A senha deve conter pelo menos 1 número e 1 letra!")
            print("==================================\n")
            continue
        else:
            print(f"Senha Atual: {nova_senha}") 
            print("==================================\n")
            time.sleep(1)
            regra3(nova_senha)
            break   

def regra3(senha_anterior):
    limpar_tela()
    print("NICE!")
    animacao_carregamento("Agora a próxima regra", 4)
    print("================================\n")
    print(f"Senha anterior: {senha_anterior}\n")

    while True:
        print("3º Regra: A senha agora deve ter letras MAIÚSCULAS >:0 !!! \n")
        nova_senha = str(input("Digite sua senha: "))
        print("")
        print(f"Senha digitada: {nova_senha}")

        # Verificando as regras anteriores
        if len(nova_senha) < 10:
            print("⚠️  A senha deve ter 10 ou mais caracteres, esqueceu? >:(")
            print("==================================\n")
            continue

        numeros = sum(1 for char in nova_senha if char.isdigit())
        letras = sum(1 for char in nova_senha if char.isalpha())
        if numeros < 1 or letras < 1:
            print("⚠️ Ops!!! A senha deve conter pelo menos 1 número e 1 letra!")
            print("==================================\n")
            continue

        # Regra 3: pelo menos uma letra maiúscula
        maiusculas = any(char.isupper() for char in nova_senha)
        if not maiusculas:
            print("⚠️ A senha deve conter pelo menos 1 letra MAIÚSCULA!")
            print("==================================\n")
            continue
        else:
            print(f"Senha Atual: {nova_senha}") 
            print("==================================\n")
            time.sleep(1)
            regra4(nova_senha)
            break  

def regra4(senha_anterior):
    limpar_tela()
    print("Perfect")
    animacao_carregamento("Agora a próxima regra", 4)
    print("================================\n")
    print(f"Senha anterior: {senha_anterior}\n")

    while True:
        print("4º Regra: A senha deve conter pelo menos 1 caractere especial (ex: !@#$%)\n")
        nova_senha = str(input("Digite sua senha: "))
        print("")
        print(f"Senha digitada: {nova_senha}")

        # Verificando as regras anteriores
        if len(nova_senha) < 10:
            print("⚠️  A senha deve ter 10 ou mais caracteres, esqueceu? >:(")
            print("==================================\n")
            continue

        numeros = sum(1 for char in nova_senha if char.isdigit())
        letras = sum(1 for char in nova_senha if char.isalpha())
        if numeros < 1 or letras < 1:
            print("⚠️ Ops!!! A senha deve conter pelo menos 1 número e 1 letra!")
            print("==================================\n")
            continue

        maiusculas = any(char.isupper() for char in nova_senha)
        if not maiusculas:
            print("⚠️ A senha deve conter pelo menos 1 letra MAIÚSCULA!")
            print("==================================\n")
            continue

        # Regra 4: pelo menos um caractere especial
        especiais = any(char in string.punctuation for char in nova_senha)
        if not especiais:
            print("⚠️ A senha deve conter pelo menos 1 caractere especial (ex: !@#$%)!")
            print("==================================\n")
            continue
        else:
            print(f"Senha Atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            regra5(nova_senha)
            break

def regra5(senha_anterior):
    limpar_tela()
    print("Oloko, você já está na regra 5?! Boa :D")
    animacao_carregamento("Agora a próxima regra", 4)
    print("================================\n")
    print(f"Senha anterior: {senha_anterior}\n")

    while True:
        print("5º Regra: Os dígitos da senha precisam somar 25!\n")
        nova_senha = str(input("Digite sua senha: "))
        print("")
        print(f"Senha digitada: {nova_senha}")

        # Verificando as regras anteriores
        if len(nova_senha) < 10:
            print("⚠️  A senha deve ter 10 ou mais caracteres, esqueceu? >:(")
            print("==================================\n")
            continue

        numeros = sum(1 for char in nova_senha if char.isdigit())
        letras = sum(1 for char in nova_senha if char.isalpha())
        if numeros < 1 or letras < 1:
            print("⚠️ Ops!!! A senha deve conter pelo menos 1 número e 1 letra!")
            print("==================================\n")
            continue

        maiusculas = any(char.isupper() for char in nova_senha)
        if not maiusculas:
            print("⚠️ A senha deve conter pelo menos 1 letra MAIÚSCULA!")
            print("==================================\n")
            continue

        especiais = any(char in string.punctuation for char in nova_senha)
        if not especiais:
            print("⚠️ A senha deve conter pelo menos 1 caractere especial (ex: !@#$%)!")
            print("==================================\n")
            continue

        # Regra 5: soma dos dígitos deve ser 25
        soma = sum(int(c) for c in nova_senha if c.isdigit())
        if soma != 25:
            print(f"⚠️ A soma dos dígitos deve ser 25 (atualmente: {soma}).")
            print("Dica: você pode ajustar os números até atingir 25.")
            print("==================================\n")
            continue
        else:
            print(f"Senha Atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            regra6(nova_senha)
            break

def regra6(senha_anterior):
    limpar_tela()
    print("Muito bom! Chegou na regra 6!")
    animacao_carregamento("Agora a próxima regra", 4)
    print("================================\n")
    print(f"Senha anterior: {senha_anterior}\n")

    while True:
        print("6º Regra: A senha deve conter um NÚMERO ROMANO entre I e X (ex: IV, VI, X).\n")
        nova_senha = str(input("Digite sua senha: "))
        print("")
        print(f"Senha digitada: {nova_senha}")

        # Verificando as regras anteriores
        if len(nova_senha) < 10:
            print("⚠️  A senha deve ter 10 ou mais caracteres, esqueceu? >:(")
            print("==================================\n")
            continue

        numeros = sum(1 for char in nova_senha if char.isdigit())
        letras = sum(1 for char in nova_senha if char.isalpha())
        if numeros < 1 or letras < 1:
            print("⚠️ Ops!!! A senha deve conter pelo menos 1 número e 1 letra!")
            print("==================================\n")
            continue

        maiusculas = any(char.isupper() for char in nova_senha)
        if not maiusculas:
            print("⚠️ A senha deve conter pelo menos 1 letra MAIÚSCULA!")
            print("==================================\n")
            continue

        especiais = any(char in string.punctuation for char in nova_senha)
        if not especiais:
            print("⚠️ A senha deve conter pelo menos 1 caractere especial (ex: !@#$%)!")
            print("==================================\n")
            continue

        # Regra 5 (reaplicada): soma dos dígitos deve ser 25
        if not soma_digitos_igual_25(nova_senha):
            soma_atual = sum(int(c) for c in nova_senha if c.isdigit())
            print(f"⚠️ A soma dos dígitos deve ser 25 (atualmente: {soma_atual}).")
            print("==================================\n")
            continue

        # Regra 6: conter número romano entre I e X
        if not contem_numero_romano(nova_senha):
            print("⚠️ A senha deve conter um número romano válido entre I e X (ex: IV, VI, X).")
            print("==================================\n")
            continue
        else:
            print(f"Senha Atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            regra7(nova_senha)
            break

def regra7(senha_anterior):
    limpar_tela()
    print("Uau! Você chegou na regra 7!")
    animacao_carregamento("Agora a próxima regra", 4)
    print("")
    animacao_carregamento("uma dica. . . Essa parte vai te irritar um pouco >;)", 2)
    print("================================\n")
    print(f"Senha anterior: {senha_anterior}\n")

    numero_alvo = random.randint(11, 99)
    alvo_str = str(numero_alvo)
    print(f"Número aleatório gerado: {alvo_str}")
    print("Você deve INCLUIR esse número na sua senha!\n")

    while True:
        print("7º Regra: Inclua o número mostrado acima dentro da senha.\n")
        nova_senha = str(input("Digite sua senha: "))
        print("")
        print(f"Senha digitada: {nova_senha}")

        # Regras anteriores
        if len(nova_senha) < 10:
            print("⚠️  A senha deve ter 10 ou mais caracteres, esqueceu? >:(")
            print("==================================\n")
            continue

        numeros = sum(1 for char in nova_senha if char.isdigit())
        letras = sum(1 for char in nova_senha if char.isalpha())
        if numeros < 1 or letras < 1:
            print("⚠️ Ops!!! A senha deve conter pelo menos 1 número e 1 letra!")
            print("==================================\n")
            continue

        maiusculas = any(char.isupper() for char in nova_senha)
        if not maiusculas:
            print("⚠️ A senha deve conter pelo menos 1 letra MAIÚSCULA!")
            print("==================================\n")
            continue

        especiais = any(char in string.punctuation for char in nova_senha)
        if not especiais:
            print("⚠️ A senha deve conter pelo menos 1 caractere especial (ex: !@#$%)!")
            print("==================================\n")
            continue

        # Regra 5 (reaplicada): soma dos dígitos deve ser 25
        if not soma_digitos_igual_25(nova_senha):
            soma_atual = sum(int(c) for c in nova_senha if c.isdigit())
            print(f"⚠️ A soma dos dígitos deve ser 25 (atualmente: {soma_atual}).")
            print("==================================\n")
            continue

        if not contem_numero_romano(nova_senha):
            print("⚠️ Ainda falta incluir um número romano válido entre I e X (ex: IV, VI, X).")
            print("==================================\n")
            continue

        # Regra 7: conter o número aleatório
        if alvo_str not in nova_senha:
            print(f"⚠️ A senha deve conter o número {alvo_str}!")
            print("==================================\n")
            continue
        else:
            print(f"Senha Atual: {nova_senha}")
            print("==================================\n")
            time.sleep(1)
            regra8(nova_senha)
            break

def regra8(senha_anterior):
    limpar_tela()
    print("Que persistência! Regra 8...")
    animacao_carregamento("Preparando algo especial", 3)
    print("================================\n")
    print(f"Senha anterior: {senha_anterior}\n")
    
    while True:
        print("8º Regra: A senha deve conter um palíndromo de pelo menos 3 letras!")
        print("Exemplo: 'ana', 'ovo', 'radar' dentro da sua senha\n")
        nova_senha = str(input("Digite sua senha: "))
        
        # Verificar todas as regras anteriores...
        if not verificar_regras_anteriores(nova_senha, ate_regra=7):
            print("==================================\n")
            continue
            
        # Nova regra: palíndromo
        if not tem_palindromo_3_chars(nova_senha):
            print("⚠️ A senha deve conter um palíndromo de 3+ letras (ex: 'ana', 'radar')!")
            print("==================================\n")
            continue
            
        print(f"Senha Atual: {nova_senha}")
        print("==================================\n")
        time.sleep(1)
        regra9(nova_senha)
        break

def regra9(senha_anterior):
    limpar_tela()
    print("Inacreditável! Regra 9...")
    animacao_carregamento("Pensando em algo diabólico", 3)
    print("================================\n")
    print(f"Senha anterior: {senha_anterior}\n")
    
    while True:
        print("9º Regra: A senha deve conter 3 dígitos em sequência crescente!")
        print("Exemplo: '123', '456', '789' dentro da sua senha\n")
        nova_senha = str(input("Digite sua senha: "))
        
        if not verificar_regras_anteriores(nova_senha, ate_regra=8):
            print("==================================\n")
            continue
            
        if not tem_sequencia_crescente(nova_senha):
            print("⚠️ A senha deve conter 3 dígitos em sequência crescente (ex: '123', '456')!")
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
        print("10º Regra: A senha deve conter um ANAGRAMA de '2024' ou '2025'!")
        print("Exemplo: '2204', '4220', '2502' etc.\n")
        nova_senha = str(input("Digite sua senha: "))
        
        if not verificar_regras_anteriores(nova_senha, ate_regra=9):
            print("==================================\n")
            continue
            
        if not tem_anagrama_ano(nova_senha):
            print("⚠️ A senha deve conter um anagrama de '2024' ou '2025'!")
            print("Dica: '2204', '4220', '2502' são válidos")
            print("==================================\n")
            continue
            
        print(f"Senha Atual: {nova_senha}")
        print("==================================\n")
        time.sleep(1)
        regra11(nova_senha)
        break

def regra11(senha_anterior):
    limpar_tela()
    print("🤯 REGRA 11! Quase lá!")
    animacao_carregamento("Preparando o grand finale", 3)
    print("================================\n")
    print(f"Senha anterior: {senha_anterior}\n")
    
    while True:
        print("11º Regra: A soma dos DÍGITOS PRIMOS (2,3,5,7) deve ser 13!")
        print("Exemplo: 2+3+5+3=13, 7+3+3=13, 5+5+3=13 etc.\n")
        nova_senha = str(input("Digite sua senha: "))
        
        if not verificar_regras_anteriores(nova_senha, ate_regra=10):
            print("==================================\n")
            continue
            
        if not soma_digitos_primos_igual_13(nova_senha):
            digitos_primos = [c for c in nova_senha if c.isdigit() and eh_primo(int(c))]
            soma_atual = sum(int(d) for d in digitos_primos)
            print(f"⚠️ A soma dos dígitos primos (2,3,5,7) deve ser 13 (atual: {soma_atual})!")
            print(f"Seus dígitos primos: {digitos_primos}")
            print("==================================\n")
            continue
            
        print(f"Senha Atual: {nova_senha}")
        print("==================================\n")
        time.sleep(1)
        regra12(nova_senha)
        break

def regra12(senha_anterior):
    limpar_tela()
    print("🎊 REGRA FINAL! A ÚLTIMA!")
    animacao_carregamento("Preparando surpresa final", 4)
    print("================================\n")
    print(f"Senha anterior: {senha_anterior}\n")
    
    while True:
        print("12º Regra: A SENHA PERFEITA!")
        print("- Deve conter TODAS as vogais (a,e,i,o,u)")
        print("- Os caracteres especiais devem formar um palíndromo")
        print("Exemplo: 'A@b#c#@' - os especiais '@#@' são simétricos\n")
        nova_senha = str(input("Digite sua senha PERFEITA: "))
        
        if not verificar_regras_anteriores(nova_senha, ate_regra=11):
            print("==================================\n")
            continue
            
        if not eh_senha_perfeita(nova_senha):
            # Dar feedback específico
            vogais_faltando = [v for v in 'aeiou' if v not in nova_senha.lower()]
            especiais = [c for c in nova_senha if c in string.punctuation]
            
            if vogais_faltando:
                print(f"⚠️ Faltam vogais: {vogais_faltando}")
            if especiais != especiais[::-1]:
                print(f"⚠️ Caracteres especiais não são simétricos: {especiais}")
            print("==================================\n")
            continue
            
        # VITÓRIA!
        print(f"\n🎉 SENHA PERFEITA: {nova_senha}")
        animacao_carregamento("PARABÉNS! VOCÊ VENCEU O JOGO!", 5)
        print("\nVocê é um verdadeiro mestre das senhas!")
        print("Obrigado por jogar! 🏆")
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