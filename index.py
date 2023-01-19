import time as tm
import os

while True:
      print('''
            Salve, salve caro usuário, vamos iniciar o programa!
            
            Para iniciar, diga como deseja que seja realizada sua contagem.
            
            C (ordem crescente) ou D (ordem decrescente).
      ''')

      ordem = str(input('Digite C (ordem crescente) ou D (ordem decrescente): '))
      if ordem[0] == "C" or ordem[0] == "c":
            print('''
            Salve, salve caro usuário, vamos iniciar a contagem.
            
            Nos conte o valor de início e final.  
            ''')
            
            inicio = int(input('Digite o valor inicial: '))
            fim = int(input('Digite o valor final: '))
            
            print('''
            Ok, já temos o valor de início e final.
            
            Agora, nos conte S para contagem SIMPLES e E para contagem ESPECIAL.
            ''')
            
            tipo = str(input('Digite S para contagem SIMPLES e E para contagem ESPECIAL: '))
            if tipo[0] == "S" or tipo[0] == "s":
                  for i in range(inicio, fim, 1):
                        print(i)
                        tm.sleep(2)
                        try:
                              os.system('cls')
                        except:
                              os.system('clear')
            elif tipo[0] == "E" or tipo[0] == "e":
                  identador = int(input('Digite o valor de passagem: '))
                  for i in range(inicio, fim, identador):
                        print(i)
                        tm.sleep(2)
                        try:
                              os.system('cls')
                        except:
                              os.system('clear')
      if ordem[0] == "D" or ordem[0] == "d":
            print('''
            Salve, salve caro usuário, vamos iniciar a contagem.
            
            Nos conte o valor de início e final.  
            ''')
            
            inicio = int(input('Digite o valor inicial: '))
            fim = int(input('Digite o valor final: '))
            
            print('''
            Ok, já temos o valor de início e final.
            
            Agora, nos conte S para contagem SIMPLES e E para contagem ESPECIAL.
            ''')
            
            tipo = str(input('Digite S para contagem SIMPLES e E para contagem ESPECIAL: '))
            if tipo[0] == "S" or tipo[0] == "s":
                  for i in range(fim, inicio, 1):
                        print(i)
                        tm.sleep(2)
                        try:
                              os.system('cls')
                        except:
                              os.system('clear')
            elif tipo[0] == "E" or tipo[0] == "e":
                  identador = int(input('Digite o valor de passagem: '))
                  for i in range(fim, inicio, identador):
                        print(i)
                        tm.sleep(2)
                        try:
                              os.system('cls')
                        except:
                              os.system('clear')
      print('''
            Deseja fazer outra contagem? S para SiM e N para NÃO!
      ''')
      if str(input('Digite S para SiM e N para NÃO: ')): break