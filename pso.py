import numpy as np

def fitness_function(x):
    # Basit bir uygunluk fonksiyonu, x'in karesini hesaplar
    return x ** 2

def pso_search(max_iter=1000, num_particles=10, num_dimensions=1, min_value=-10, max_value=10):
    # Başlangıç pozisyonları ve hızları rastgele belirlenir
    positions = np.random.uniform(low=min_value, high=max_value, size=(num_particles, num_dimensions))
    velocities = np.random.uniform(low=-1, high=1, size=(num_particles, num_dimensions))
    pbest = positions.copy()  # Her parçacığın en iyi konumu, başlangıçta kendi pozisyonuna eşittir
    gbest = positions[np.argmin(fitness_function(positions))]  # Sürünün en iyi konumu, başlangıçta rastgele bir konumdan seçilir

    for _ in range(max_iter):
        for i in range(num_particles):
            # Parçacıkların hızı ve konumu güncellenir
            velocities[i] = 0.5 * velocities[i] + 0.5 * np.random.uniform(0, 1) * (pbest[i] - positions[i]) + \
                            0.5 * np.random.uniform(0, 1) * (gbest - positions[i])
            positions[i] += velocities[i]
            
            # Parçacığın yeni konumu için uygunluk değeri hesaplanır
            fitness_val = fitness_function(positions[i])
            
            # Parçacığın en iyi konumu güncellenir
            if fitness_val < fitness_function(pbest[i]):
                pbest[i] = positions[i].copy()
                
                # Parçacığın en iyi konumu, sürünün en iyi konumu ile karşılaştırılır
                if fitness_val < fitness_function(gbest):
                    gbest = positions[i].copy()

    return gbest


solution = pso_search()
print("Optimum çözüm:", solution)
print("Uygunluk değeri:", fitness_function(solution))
