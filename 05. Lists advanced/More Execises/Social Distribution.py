population = list(map(int, input().split(", ")))
min_wealth = int(input())
condition = False

for el in range(len(population)):
    richest = max(population)
    if population[el] < min_wealth:
        for i in range(len(population)):
            if population[i] == richest:
                population[i] -= min_wealth - population[el]
                if population[i] >= min_wealth:
                    population[el] = min_wealth
                else:
                    print("No equal distribution possible")
                    condition = True
                    break
    if condition:
        break
if condition:
    pass
else:
    print(population)