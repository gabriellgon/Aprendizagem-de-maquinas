import numpy as np
import matplotlib.pyplot as plt

# Função de ativação sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada da função sigmoid
def derivada_sigmoid(x):
    return x * (1 - x)

# Dados de entrada e saída
X = np.array([[0], [0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9], [1.0]])
T = np.array([[-0.9602], [-0.5770], [-0.0729], [-0.3771], [0.6405], [0.6600], [0.4609], [0.1336], [-0.2013], [-0.4344], [-0.5000]])

# Normalização dos dados de saída
T_normalizado = (T - np.min(T)) / (np.max(T) - np.min(T))

# Configuração da rede neural
tamanho_entrada = 1
tamanho_oculta = 4
tamanho_saida = 1
taxa_aprendizado = 0.1
epocas = 70000

# Inicialização dos pesos com média zero e desvio padrão adequado
np.random.seed(1)
pesos_entrada_oculta = np.random.normal(0, 1, size=(tamanho_entrada, tamanho_oculta))
pesos_oculta_saida = np.random.normal(0, 1, size=(tamanho_oculta, tamanho_saida))

# Listas para armazenar os erros
historico_erro = []

# Treinamento da rede neural
for epoca in range(epocas):
    # Forward pass
    entrada_oculta = np.dot(X, pesos_entrada_oculta)
    saida_oculta = sigmoid(entrada_oculta)
    entrada_saida = np.dot(saida_oculta, pesos_oculta_saida)
    saida_final = sigmoid(entrada_saida)
    
    # Cálculo do erro
    erro = T_normalizado - saida_final
    historico_erro.append(np.mean(np.abs(erro)))
    
    # Retropropagação
    delta_saida = erro * derivada_sigmoid(saida_final)
    erro_oculta = delta_saida.dot(pesos_oculta_saida.T)
    delta_oculta = erro_oculta * derivada_sigmoid(saida_oculta)
    
    # Atualização dos pesos
    pesos_oculta_saida += saida_oculta.T.dot(delta_saida) * taxa_aprendizado
    pesos_entrada_oculta += X.T.dot(delta_oculta) * taxa_aprendizado

# Plotando o erro quadrático ao longo das épocas
plt.plot(range(epocas), historico_erro)
plt.xlabel('Época')
plt.ylabel('Erro Quadrático Médio')
plt.title('Erro Quadrático Médio ao Longo das Épocas')
plt.show()

# Avaliação da função final
X_teste = np.arange(0, 1.1, 0.1).reshape(-1, 1)
entrada_oculta_teste = np.dot(X_teste, pesos_entrada_oculta)
saida_oculta_teste = sigmoid(entrada_oculta_teste)
entrada_saida_teste = np.dot(saida_oculta_teste, pesos_oculta_saida)
saida_final_teste = sigmoid(entrada_saida_teste)

# Desnormalização dos resultados para comparar com os dados originais
saida_final_teste = saida_final_teste * (np.max(T) - np.min(T)) + np.min(T)

# Plotando a função final e o teste da rede treinada
plt.scatter(X, T, label='Dados de Treinamento')
plt.plot(X_teste, saida_final_teste, label='Função Aproximada', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Aproximação da Função por MLP e Teste da Rede')
plt.legend()
plt.show()

# Teste da rede treinada para todos os pontos de entrada X
entrada_oculta_teste_todos = np.dot(X, pesos_entrada_oculta)
saida_oculta_teste_todos = sigmoid(entrada_oculta_teste_todos)
entrada_saida_teste_todos = np.dot(saida_oculta_teste_todos, pesos_oculta_saida)
saida_final_teste_todos = sigmoid(entrada_saida_teste_todos)

# Desnormalização dos resultados para comparar com os dados originais
saida_final_teste_todos = saida_final_teste_todos * (np.max(T) - np.min(T)) + np.min(T)

print("\nTeste da Rede Neural para Todos os Pontos de Entrada:")
print("Entradas de teste:", X.flatten())
print("Saídas previstas:", saida_final_teste_todos.flatten())