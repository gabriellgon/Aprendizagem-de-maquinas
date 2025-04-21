import numpy as np

def rastrigin(x):
    A = 10
    return A * len(x) + np.sum(x**2 - A * np.cos(2 * np.pi * x))

def differential_evolution(objective_function, bounds, population_size=100, max_generations=100, crossover_rate=0.7, differential_weight=0.8):
    dimension = len(bounds)
    
    # Inicialização da população
    population = np.random.uniform(bounds[:, 0], bounds[:, 1], size=(population_size, dimension))
    
    for generation in range(max_generations):
        for i in range(population_size):
            # Seleção de três indivíduos diferentes
            candidates = np.random.choice(population_size, 3, replace=False)
            a, b, c = population[candidates]
            
            # Crossover e mutação
            trial_vector = a + differential_weight * (b - c)
            mask = np.random.rand(dimension) < crossover_rate
            trial_vector[mask] = population[i, mask]
            
            # Avaliação do vetor de teste
            f_original = objective_function(population[i])
            f_trial = objective_function(trial_vector)
            
            # Atualização da população
            if f_trial < f_original:
                population[i] = trial_vector
        
    # Retorno do melhor indivíduo encontrado
    best_index = np.argmin([objective_function(ind) for ind in population])
    best_solution = population[best_index]
    best_fitness = objective_function(best_solution)
    
    return best_solution, best_fitness

# Definindo os limites para a função de Rastrigin
bounds = np.array([[-5.12, 5.12], [-5.12, 5.12]])

# Executando a evolução diferencial para minimizar a função de Rastrigin
best_solution, best_fitness = differential_evolution(rastrigin, bounds)

# Exibindo os resultados
print("Melhor solução encontrada:", best_solution)
print("Melhor valor de aptidão encontrado:", best_fitness)
