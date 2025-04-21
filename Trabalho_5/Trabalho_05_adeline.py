import matplotlib.pyplot as plt
import numpy as np

x = [[2.215,0.224,0.294,2.327,2.497,0.169,1.274,1.526,2.009,1.759,1.367,2.173,0.856,2.21,1.587,0.35,1.441,0.185,2.764,1.947],
     [2.063,1.586,0.651,2.932,2.322,1.943,2.428,0.596,2.161,0.342,0.938,2.719,1.904,1.868,1.642,0.84,0.09,1.327,1.149,1.598]]

t = [-1,1,1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,1,1,1,-1,-1]

#w_ant =  np.random.uniform(-0.5,0,5)
w_ant = 0.5-np.random.rand(1,2)
b_ant = 0.5-np.random.rand(1)
wnovo = np.zeros((1,2))
bnovo = np.zeros((1))

print(w_ant)
print(b_ant)

teta = 0
alfa = 0.05
numciclos = 200
ciclos = 0

erroquadratico = 0
ciclos = ciclos+1
while ciclos<=numciclos:
    erroquadratico=0
    ciclos = ciclos+1
    for i in range(20):
      #y_liquido = w_ant[0][0]*x[0][i]+ w_ant[0][1]*x[1][i] + b_ant[0]
      y_liquido = w_ant[0][0]*x[0][i] + w_ant[0][1]*x[1][i] + b_ant[0]
      # Função de ativação linear
      y = y_liquido
      # Cálculo do erro quadratico
      erroquadratico = erroquadratico + (t[i]-y)**2
      # Atualização dos pesos
      wnovo[0][0] = w_ant[0][0] + alfa * (t[i]-y)*x[0][i]
      wnovo[0][1] = w_ant[0][1] + alfa * (t[i]-y)*x[1][i]
      bnovo[0] = b_ant[0] + alfa * (t[i]-y)

      w_ant = wnovo
      b_ant = bnovo
    plt.plot(ciclos,erroquadratico,'ro')
plt.show()

  # Teste da rede treinada
for i in range(20):
  y_liquido = wnovo[0][0] * x[0][i] + wnovo[0][1] * x[1][i] + bnovo[0]
  # Função de ativação para o teste: degrau
  if y_liquido >= teta:
    y = 1
  else:
    y = -1
  print(i,"Target:",t[i],"Saída:",y)
  print(i,"Target:",t[i],"Saída liquida: ",y_liquido)