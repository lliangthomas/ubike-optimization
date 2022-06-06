from tabulate import tabulate
import math

def poisson_formula(mean_number, whole_number):
    return ((pow(mean_number, whole_number)*math.exp(-mean_number))/math.factorial(whole_number))

def part_1(S, A_AVG, L_AVG):
    table = [["Probability", "B: Initial Number of U-Bikes"]]
    for B in range(0, S+1):
        probability = 0
        for A in range(0, A_AVG+101):
            for L in range(0, L_AVG+101): 
                if ((A-L) > S - B):
                    probability += poisson_formula(A_AVG, A) * poisson_formula(L_AVG, L)
                if ((L-A) > B):
                    probability += poisson_formula(A_AVG, A) * poisson_formula(L_AVG, L)
        if probability != 0:
            table.append([probability, B])
    print (tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    del table[0]
    print ("Optimal Value of B is {} with a probability of {}".format(min(table)[1], min(table)[0]))

def part_2_no_normalise(A_AVG, L_AVG):
    table = [["Probability", "S: Number of Available Slots"]]
    for S in range(1, 151):
        avg_probability = 0
        for B in range(0, S+1):
            probability = 0
            for A in range(0, A_AVG+101):
                for L in range(0, L_AVG+101):
                    if ((A-L) > S - B):
                        probability += poisson_formula(A_AVG, A) * poisson_formula(L_AVG, L)
                    if ((L-A) > B):
                        probability += poisson_formula(A_AVG, A) * poisson_formula(L_AVG, L) 
            if probability != 0:
                avg_probability += probability
        avg_probability = avg_probability / (S)
        table.append([avg_probability, S])
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    print (tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    del table[0]
    print ("Optimal Value of S is {} with a probability of {}".format(min(table)[1], min(table)[0]))

def part_2(C, A_AVG, L_AVG):
    table = [["Probability", "S: Number of Available Slots", "B: Initial Number of U-Bikes"]]
    for S in range(1, 201):
        for B in range(0, S+1): 
            probability = 0
            for A in range(0, A_AVG+101):
                for L in range(0, L_AVG+101): 
                    if ((A-L) > S - B):
                        probability += poisson_formula(A_AVG, A) * poisson_formula(L_AVG, L) 
                    if ((L-A) > B):
                        probability += poisson_formula(A_AVG, A) * poisson_formula(L_AVG, L) 
            if probability != 0:
                probability += (S/C)
                table.append([probability, S, B])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    del table[0]
    print ("Optimal Pair is S = {} and B = {}, with a probability of {}".format(min(table)[1], min(table)[2], min(table) [0]))

part_1(2, 19, 24)
part_2_no_normalise(19, 24)
part_2(300000, 19, 24)