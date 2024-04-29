import random 
def binToDec(chromosome):
    return int(chromosome, 2)
def decToBin(chromosome):
    return bin(chromosome)[2:].zfill(5)

def crossover(population, crossover_rate):
    offSpring = []
    for i in range(0, len(population), 2):
        p1 = population[i]
        p2 = population[i + 1] 
        
        if random.random() < crossover_rate:
            crossover_point = random.randint(1, len(p1) - 1)
            offspring1 = p1[crossover_point:] + p2[:crossover_point]
            offspring2 = p2[crossover_point:] + p1[:crossover_point]
            
            offSpring.extend([offspring1, offspring2])
        else:
            offSpring.extend([p1, p2])
            
    return offSpring
    
if __name__ == "__main__":
    population = [10, 6,3,4,1,2]
    crossover_rate = 0.25
    
    print("Initial population: ")
    for chromosome in population:
        print(f'Binary: {decToBin(chromosome)}, Decimal: {chromosome}, ')
    
    for i in range(len(population)):
        population[i] = decToBin(population[i])
        
    offSpring = crossover(population, crossover_rate)
    
    print("Final population: ")
    for chromosome in offSpring:
        print(f'Binary: {chromosome}, Decimal: , {binToDec(chromosome)}')
