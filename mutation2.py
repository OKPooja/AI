import random 

def decToBin(chromosome):
    return bin(chromosome)[2:].zfill(5)

def binToDec(chromosome):
    return int(chromosome, 2)
    
def mutation(population, mutation_rate):
    for i in range(len(population)):
        if random.random() < mutation_rate:
            mutationPoint = random.randint(0, 4)
            chromosome_list = list(population[i])  
            chromosome_list[mutationPoint] = '1' if  chromosome_list[mutationPoint] == '0' else '0'  
            population[i] = ''.join(chromosome_list)  

if __name__ == "__main__":
    population = []
    mutation_rate = 0.1
    for _ in range(0, 6):
        population.append(random.randint(0, 15))
    
    print("Before Mutation: ")
    for chromosome in population:
        print(f'Binary: {decToBin(chromosome)}, Decimal: {chromosome}, ')
     
    for i in range(len(population)):
        population[i] = decToBin(population[i])   
        
    mutation(population, mutation_rate)
    
    print("After Mutation: ")
    for chromosome in population:
        print(f'Binary: {chromosome}, Decimal: {binToDec(chromosome)}')
