import random 
def decToBin(chromosome):
    return bin(chromosome)[2:].zfill(5)

def mutation(population, mutation_rate):
    for i in range(len(population)):
        if random.random() < mutation_rate:
            mutationPoint = random.randint(0,4)
            leftShift = 1 << mutationPoint
            population[i] = population[i] ^ leftShift

if __name__ == "__main__":
    #population = [10,6,3,4,1,2]
    population = []
    mutation_rate = 0.1
    for _ in range(0, 6):
        population.append(random.randint(0, 15))
    print("Before Mutation: ")
    for chromosome in population:
        print(f'Decimal: {chromosome}, Binary: {decToBin(chromosome)}')
        
    mutation(population, mutation_rate)
    
    print("After Mutation: ")
    for chromosome in population:
        print(f'Decimal: {chromosome}, Binary: {decToBin(chromosome)}')
