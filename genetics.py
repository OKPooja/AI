import random

def initialize_population(no_of_chromosomes, num_variables):

    population = []
    for i in range(no_of_chromosomes):
        temp = []
        for j in range(num_variables):
            temp.append(random.randint(0,15))
        population.append(temp)
    
    return population

def fitness(population):

    fitness_values = []
    #a + 2*b + 3*c + 4*d
    for variables in population:
        a,b,c,d = variables
        value = abs((a + 2 * b + 3 * c + 4 * d) - 30)
        fitness_values.append(value)

    return fitness_values

def selection(fitness_values, population):
    n = len(population)
    selected_population = []
    total_sum = 0
    probabilites = []
    #Calculate fitness ratio and total sum of the ratio
    for i in range(len(fitness_values)):
        fitness_values[i] = (1/(1 + fitness_values[i]))
        total_sum += fitness_values[i]
    #Caculate probability
    for i in range(len(fitness_values)):
        probabilites.append(fitness_values[i]/total_sum)
    #Caluclate cumulative frequency
    cumulative = [probabilites[0]]
    for i in range(1, len(probabilites)):
        cumulative.append(cumulative[i - 1] + probabilites[i])
    #Assign random number between 0-1
    rand = [random.random() for i in range(n)]

    for i in range(n):
        j = 0
        while j < n:
            if j + 1 < n and rand[i] > cumulative[j] and rand[i] < cumulative[j + 1]:
                selected_population.append(population[j + 1])
                break
            else:
                j += 1
        if j == n:
            selected_population.append(population[0])

    return selected_population

def crossover(selected_population, crossover_rate):
    offSpring = []
    for i in range(0, len(selected_population), 2):
        p1 = selected_population[i]
        p2 = selected_population[i + 1] 
        
        if random.random() < crossover_rate:
            crossover_point = random.randint(1, len(p1) - 1)
            offspring1 = p1[crossover_point:] + p2[:crossover_point]
            offspring2 = p2[crossover_point:] + p1[:crossover_point]
            
            offSpring.extend([offspring1, offspring2])
        else:
            offSpring.extend([p1, p2])
            
    return offSpring

def mutation(crossover_population, mutation_rate):
    mutation_population = []
    for i in range(len(crossover_population)):
        if random.random() < mutation_rate:
            index = random.randint(0, len(crossover_population[i]) - 1)
            new_value = random.randint(0, 30)
            crossover_population[i][index] = new_value
            mutation_population.append(crossover_population[i])
        else:
            mutation_population.append(crossover_population[i])

    return mutation_population

def genetics(no_of_chromosomes, mutation_rate, crossover_rate, num_variables):

    #Step 1: Initialize population
    population = initialize_population(no_of_chromosomes, num_variables)
    i = 1
    while True:

        #Step 2: Calculate fitness values
        fitness_values = fitness(population)

        best_chromosome = population[fitness_values.index(min(fitness_values))]
        if min(fitness_values) == 0:
            print(f"Optimal Solution found after {i} Generations")
            print(f"Generation {i}: Best solution: {best_chromosome}, Fitness: {min(fitness_values)}")
            break

        i = i + 1

        #Step 3: Selection
        selected_population = selection(fitness_values, population)
        #print(f'Selected population: {selected_population}')

        #Step 4: Crossover
        crossover_population = crossover(selected_population, crossover_rate)
        #print(f'Crossover population: {crossover_population}')

        #Step 5: Mutatuon
        mutation_population = mutation(crossover_population, mutation_rate)
        #print(f'Mutated population: {mutation_population}')

        population = mutation_population
        
if __name__ == "__main__":  
    no_of_chromosomes = 6
    mutation_rate = 0.10
    crossover_rate = 0.25
    num_variables = 4
    genetics(no_of_chromosomes, mutation_rate, crossover_rate, num_variables)
