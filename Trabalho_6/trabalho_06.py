def lertxt(nome):
    coluna1 = []
    coluna2 = []
    # Abra o arquivo .txt em modo de leitura
    with open(nome, 'r') as arquivo:
        # Leia cada linha do arquivo
        next(arquivo)
        for linha in arquivo:
            # Divida a linha em duas partes usando o caractere de separação (por exemplo, espaço ou vírgula)
            valores = linha.strip().split()  # Você pode usar split(',') se as colunas forem separadas por vírgula
            # Verifique se há pelo menos duas partes (colunas) na linha
            if len(valores) >= 2:
                # Adicione o valor da primeira coluna ao vetor coluna1
                coluna1.append(float(valores[0]))
                # Adicione o valor da segunda coluna ao vetor coluna2
                coluna2.append(float(valores[1]))
    # Agora, coluna1 contém os valores da primeira coluna e coluna2 contém os valores da segunda coluna
    return (coluna1, coluna2)

def soma_y_ao_quadrado(t):
  aux = 0
  soma = 0
  for i in range(50):
    aux = t[i]**2 + aux
  soma = aux
  return (soma)

def soma_xy(x,t):
  aux = 0
  soma = 0
  for i in range(len(x)):
    aux = x[i] * t[i] + aux
  soma = aux
  return (soma)

def soma_x_ao_quadrado(x):
  aux = 0
  soma = 0
  for i in range(len(x)):
    aux = x[i]**2 + aux
  soma = aux
  return (soma)

def soma_x(x):
  aux = 0
  soma = 0
  for i in range(len(x)):
    aux = x[i] + aux
  soma = aux
  return (soma)

def soma_y(t):
  aux = 0
  soma = 0
  for i in range(50):
    aux = t[i] + aux
  soma = aux
  return (soma)

def plotar_fronteira_axmaisb(a,b,x,t):
  for abscissa in np.arange(-4,11, 0.1):
    ordenada = abscissa*b + a
    plt.plot(abscissa,ordenada,'r.')
    #plt.rcParams['figure.figsize'] = (24,16)
    for i in range(0,50,1):
      plt.plot(x[i],t[i],'b*')
      plt.title('Regressão Linear Simples')
      plt.xlabel('Força de trabalho (Xi)')
      plt.ylabel('Tempo de execução (Yi)')
  return

def plotar_fronteira(w_novo,b_novo,a,b,x,t):
  for abscissa in np.arange(-4,11, 0.1):
    ordenadaa = abscissa*wnovo[0] + bnovo[0]
    plt.plot(abscissa,ordenadaa,'g.')
    #plt.rcParams['figure.figsize'] = (24,16)
    for i in range(0,50,1):
      plt.plot(x[i],t[i],'b*')
      plt.title('Adaline')
      plt.xlabel('Força de trabalho (Xi)')
      plt.ylabel('Tempo de execução (Yi)')
  return

import math
import matplotlib.pyplot as plt
import numpy as np

nome_do_arquivo = 'basedeobservacoes.txt'
x ,t = lertxt(nome_do_arquivo)

#w_ant =  np.random.uniform(-0.5,0,5)
w_ant = 0.5-np.random.rand(1)
b_ant = 0.5-np.random.rand(1)
wnovo = np.zeros((1))
bnovo = np.zeros((1))

teta = 0
#alfa = 0.0015
alfa = 0.0010
numciclos = 3000
ciclos = 0
while ciclos<numciclos:
    erroquadratico = 0
    ciclos = ciclos+1
    for i in range(len(x)):
      #y_liquido = w_ant[0][0]*x[0][i]+ w_ant[0][1]*x[1][i]+ b_ant[0]
      y_liquido = w_ant[0]*x[i] + b_ant[0]

      y = y_liquido
      # Cálculo do erro quadratico
      erroquadratico = erroquadratico + (t[i]-y)**2
      # Atualização dos pesos
      wnovo[0] = w_ant[0] + alfa * (t[i]-y)*x[i]
      bnovo[0] = b_ant[0] + alfa * (t[i]-y)

      w_ant = wnovo
      b_ant = bnovo
    print(erroquadratico,ciclos)
    plt.plot(ciclos,erroquadratico,'ro')
    plt.title('Ciclos x Erro quadrático')
    plt.xlabel('Ciclos')
    plt.ylabel('Erro quadrático')
plt.show()


# Calculo de B pelo metodo de regressão linear

b = (len(x)*(soma_xy(x,t))-((soma_x(x))*(soma_y(t))))/(len(x)*(soma_x_ao_quadrado(x))-(soma_x(x))**2)


#Calculo de A pelo metodo de regressão linear

a = soma_y(t)/len(x) - b*(soma_x(x)/len(x))


# Coeficiente de correlação R (relação entre as variaveis x, y)
r =(len(x)*soma_xy(x,t)-(soma_x(x)*(soma_y(t))))/(math.sqrt(len(x)*(soma_x_ao_quadrado(x))-(soma_x(x))**2)*(math.sqrt(len(x)*(soma_y_ao_quadrado(t))-(soma_y(t))**2)))

plotar_fronteira_axmaisb(a,b,x,t)
plt.show()
plotar_fronteira(wnovo,bnovo,a,b,x,t)
#plt.legend(['Adalaine','Regressão Linear Simples','Pontos de x e y'],loc='upper left')
plt.show()

#Verificar a correlação

if (r < 0):
  print('Quanto mais próximo de -1, maior é a correlação negativa',"|| ","R: ", r)
elif (r == 0):
  print('Quanto mais próximo de 0, menor é a correlação linear',"|| ","R: ", r)
elif (r > 0):
  print('Quanto mais próximo de 1, maior é a correlação positiva',"|| ","R: ", r)

print("a: ",a,"||","b: ",b,"||","r: ",r)
print("a: ",wnovo,"b: ",bnovo)