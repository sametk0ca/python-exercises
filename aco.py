import random

# ACO parametreleri
NUM_ANTS = 5
NUM_ITERATIONS = 20
ALPHA = 1.0  # Feromon yoğunluğunun etkisi
BETA = 2.0   # Uzaklığın etkisi
EVAPORATION_RATE = 0.5

# Grafiğin temsili
graph = {
    'A': {'B': 5, 'C': 7, 'D': 10},
    'B': {'A': 5, 'C': 8, 'D': 6},
    'C': {'A': 7, 'B': 8, 'D': 9},
    'D': {'A': 10, 'B': 6, 'C': 9}
}

# Başlangıç durumu
pheromones = {(i, j): 1 for i in graph for j in graph[i]}

# Uzaklık matrisi oluşturma
distances = {}
for node1 in graph:
    for node2 in graph[node1]:
        distances[(node1, node2)] = graph[node1][node2]

# Yol bulma
def find_path(graph, pheromones, distances):
    path = []
    current_node = random.choice(list(graph.keys()))
    path.append(current_node)

    for _ in range(len(graph) - 1):
        next_node = select_next_node(graph, pheromones, distances, current_node, path)
        path.append(next_node)
        current_node = next_node

    return path

# Bir sonraki düğümü seçme
def select_next_node(graph, pheromones, distances, current_node, path):
    unvisited_nodes = [node for node in graph[current_node] if node not in path]
    probabilities = []

    for node in unvisited_nodes:
        pheromone = pheromones[(current_node, node)]
        distance = distances[(current_node, node)]
        probability = (pheromone ** ALPHA) * ((1 / distance) ** BETA)
        probabilities.append(probability)

    total_probability = sum(probabilities)
    probabilities = [prob / total_probability for prob in probabilities]
    next_node = random.choices(unvisited_nodes, weights=probabilities)[0]

    return next_node

# Feromon izlerini güncelleme
def update_pheromones(graph, pheromones, paths):
    for key in pheromones.keys():
        pheromones[key] *= (1 - EVAPORATION_RATE)

    for path in paths:
        for i in range(len(path) - 1):
            pheromones[(path[i], path[i+1])] += 1

# ACO algoritması
def ant_colony_optimization(graph, pheromones, distances, num_ants, num_iterations):
    best_path = None
    best_distance = float('inf')

    for _ in range(num_iterations):
        paths = [find_path(graph, pheromones, distances) for _ in range(num_ants)]
        update_pheromones(graph, pheromones, paths)
        current_best_path = min(paths, key=lambda x: calculate_distance(x, distances))
        current_best_distance = calculate_distance(current_best_path, distances)

        if current_best_distance < best_distance:
            best_path = current_best_path
            best_distance = current_best_distance

    return best_path, best_distance

# Mesafe hesaplama
def calculate_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[(path[i], path[i+1])]
    return total_distance

# ACO'yu çalıştırma
best_path, best_distance = ant_colony_optimization(graph, pheromones, distances, NUM_ANTS, NUM_ITERATIONS)
print("En iyi yol:", best_path)
print("En iyi mesafe:", best_distance)
