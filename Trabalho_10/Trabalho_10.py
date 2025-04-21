import numpy as np
import matplotlib.pyplot as plt

# Dados de entrada
data = np.loadtxt('observacoescluster.txt')

# Função para calcular a distância euclidiana entre dois pontos
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Função para inicializar os centróides de forma aleatória
def initialize_centroids(data, k):
    indices = np.random.choice(len(data), k, replace=False)
    return data[indices]

# Função para atribuir pontos aos clusters
def assign_to_clusters(data, centroids):
    clusters = [[] for _ in range(len(centroids))]
    
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster = np.argmin(distances)
        clusters[cluster].append(point)
    
    return clusters

# Função para atualizar os centróides
def update_centroids(clusters):
    new_centroids = [np.mean(cluster, axis=0) for cluster in clusters]
    return new_centroids

# Função para calcular o erro quadrático total (SSE)
def calculate_sse(data, centroids, clusters):
    sse = 0
    for i, centroid in enumerate(centroids):
        cluster = clusters[i]
        sse += np.sum([euclidean_distance(point, centroid) ** 2 for point in cluster])
    return sse

# Função para plotar os clusters e centróides
def plot_clusters(data, centroids, clusters):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    
    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        plt.scatter(cluster[:, 0], cluster[:, 1], c=colors[i])
    
    centroids = np.array(centroids)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='x')
    
    plt.legend()
    plt.title('Agrupamento com K-Means')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.show()

# Configuração do K-Means
k = 4  # Número de clusters
max_iterations = 100
tolerance = 1e-4

# Inicialização dos centróides
centroids = initialize_centroids(data, k)

sse_values = []
for iteration in range(max_iterations):
    # Atribuir pontos aos clusters
    clusters = assign_to_clusters(data, centroids)
    
    # Calcular o novo SSE
    sse = calculate_sse(data, centroids, clusters)
    sse_values.append(sse)
    
    # Atualizar os centróides
    new_centroids = update_centroids(clusters)
    
    # Verificar critério de convergência
    if np.all(np.abs(np.array(new_centroids) - np.array(centroids)) < tolerance):
        break
    
    centroids = new_centroids

# Plotar os clusters e centróides
plot_clusters(data, centroids, clusters)

# Plotar o gráfico de erro quadrático total
plt.plot(range(1, len(sse_values) + 1), sse_values, marker='o')
plt.title('Erro Quadrático Total (SSE) vs. Número de Clusters')
plt.xlabel('Número de Clusters')
plt.ylabel('Erro Quadrático Total (SSE)')
plt.show()