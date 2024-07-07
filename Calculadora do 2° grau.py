import math

Decisao_Do_Usuario = int(input('Se você deseja inserir os coeficientes da equação para receber o valor digite [1], mas se você preferir digitar os resultados e receber a equação digite [2]: '))

if Decisao_Do_Usuario == 1:
    # Pedindo ao usuário para inserir os valores dos coeficientes
    a = float(input('Insira um valor para A: '))
    b = float(input('Insira um valor para B: '))
    c = float(input('Insira um valor para C: '))

    # Calculando o delta
    delta = (b**2) - (4*a*c)

    # Verificando se há raízes reais
    if delta < 0:
        print("A equação não possui raízes reais.")
    else:
        # Calculando as raízes usando a fórmula de Bhaskara
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        
        # Exibindo os resultados
        print(f"As raízes da equação são: {x1} e {x2}")

elif Decisao_Do_Usuario == 2:
    def encontrar_equacao(a, x1, x2):
        # Assumimos que a = 1 para simplificar
        a = 1
        b = -a * (x1 + x2)
        c = a * x1 * x2
        
        # Montando a equação
        equacao = f"{a}x^2 + {b}x + {c} = 0"
        
        return equacao
    
    # Pedindo ao usuário para digitar as raízes da equação
    x1 = float(input('Digite a primeira raiz da equação: '))
    x2 = float(input('Digite a segunda raiz da equação: '))
    
    # Chamando a função para encontrar a equação do segundo grau
    equacao = encontrar_equacao(x1, x2)
    print(f"A equação do segundo grau com raízes {x1} e {x2} é:")
    print(equacao)

else:
    print('Digite 1 ou 2')

   


