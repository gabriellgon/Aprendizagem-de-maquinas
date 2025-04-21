import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a distância euclidiana entre dois pontos
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Função para inicializar os centróides usando K-Means++
def initialize_centroids_kmeans_pp(data, k):
    centroids = [data[np.random.choice(len(data))]]
    for _ in range(1, k):
        distances = np.array([min([euclidean_distance(point, centroid) for centroid in centroids]) for point in data])
        probabilities = distances / distances.sum()
        cumulative_probabilities = probabilities.cumsum()
        r = np.random.rand()
        for j, p in enumerate(cumulative_probabilities):
            if r < p:
                centroids.append(data[j])
                break
    return np.array(centroids)

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

# Função para executar o K-Means
def kmeans(data, k, max_iterations=100, tolerance=1e-4, init_method='random'):
    if init_method == 'kmeans++':
        centroids = initialize_centroids_kmeans_pp(data, k)
    else:
        centroids = np.random.permutation(data)[:k]
    
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

    return centroids, clusters, sse_values

# Função para plotar os clusters e centróides
def plot_clusters(data, centroids, clusters, title):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    
    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        plt.scatter(cluster[:, 0], cluster[:, 1], c=colors[i])
    
    centroids = np.array(centroids)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='x')
    
    plt.legend()
    plt.title(title)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.show()

# Ler dados do arquivo de texto
data = np.loadtxt('observacoescluster.txt')

# Configuração do K-Means
k = 4  # Número de clusters
max_iterations = 100
tolerance = 1e-4

# Executar o K-Means com inicialização aleatória
centroids_random, clusters_random, sse_values_random = kmeans(data, k, max_iterations, tolerance, 'random')

# Executar o K-Means com inicialização K-Means++
centroids_kmeans_pp, clusters_kmeans_pp, sse_values_kmeans_pp = kmeans(data, k, max_iterations, tolerance, 'kmeans++')

# Plotar os clusters e centróides para inicialização aleatória
plot_clusters(data, centroids_random, clusters_random, 'Agrupamento com K-Means (Inicialização Aleatória)')

# Plotar os clusters e centróides para inicialização K-Means++
plot_clusters(data, centroids_kmeans_pp, clusters_kmeans_pp, 'Agrupamento com K-Means (Inicialização K-Means++)')

# Plotar o gráfico de erro quadrático total para ambas as inicializações
plt.plot(range(1, len(sse_values_random) + 1), sse_values_random, marker='o', label='Aleatório')
plt.plot(range(1, len(sse_values_kmeans_pp) + 1), sse_values_kmeans_pp, marker='o', label='K-Means++')
plt.title('Erro Quadrático Total (SSE) vs. Número de Clusters')
plt.xlabel('Número de Clusters')
plt.ylabel('Erro Quadrático Total (SSE)')
plt.legend()
plt.show()
